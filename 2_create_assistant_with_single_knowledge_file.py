from dotenv import load_dotenv
load_dotenv()
import os
from openai import OpenAI
from PyPDF2 import PdfReader

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

vector_store_name = "COMMAND General Info"

# Create Vector Store
vector_store = client.beta.vector_stores.create(name=vector_store_name)
print(f"Vector Store Id - {vector_store.id}")

pdf_path = "knowledge/COMMAND_information.pdf"

# Extract text from the PDF file
reader = PdfReader(pdf_path)
text = ""
for page in reader.pages:
    text += page.extract_text()

# Save the extracted text to a temporary file
temp_file_path = "COMMAND_information.txt"
with open(temp_file_path, "w") as temp_file:
    temp_file.write(text)

# Upload the temporary file to the vector store
file_stream = open(temp_file_path, "rb")
file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
    vector_store_id=vector_store.id,
    files=[file_stream]
)
file_stream.close()

# Check the status of the file
print(f"File status: {file_batch.status}")

assistant_description = "You are an assistant specialized in qualifying and generating leads for COMMAND LABS - a software laboratory."
assistant_model = "gpt-4-turbo"

# Create a new assistant
assistant = client.beta.assistants.create(
    description=assistant_description,
    model=assistant_model,
    name=vector_store_name,
)

print(f"New assistant created with ID: {assistant.id}")
print(f"New vector store created with ID: {vector_store.id}")

# Update the assistant with the vector store
updated_assistant = client.beta.assistants.update(
    assistant_id=assistant.id,
    tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}}
)
print("Assistant updated with vector store!")

# Create a thread
thread = client.beta.threads.create()
print(f"Your thread ID is - {thread.id}")

# Clean up the temporary file
os.remove(temp_file_path)