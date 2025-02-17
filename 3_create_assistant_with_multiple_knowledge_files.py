from dotenv import load_dotenv
load_dotenv()
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

vector_store_name = "COMMAND KB"

# Create Vector Store
vector_store = client.beta.vector_stores.create(name=vector_store_name)
print(f"Vector Store Id - {vector_store.id}")

file_path1 = "knowledge/COMMAND_information.pdf"
file_path2 = "knowledge/COMMAND_skills.pdf"

file_paths = [file_path1, file_path2]

file_ids = []
for file_path in file_paths:
    with open(file_path, "rb") as file:
        response = client.files.create(file=file, purpose="assistants")
        file_ids.append(response.id)

vector_store_file_batch = client.beta.vector_stores.file_batches.create(
    vector_store_id=vector_store.id,
    file_ids=file_ids
)
print(f"File Batch ID: {vector_store_file_batch.id}")
print(f"File Batch Status: {vector_store_file_batch.status}")

assistant_description = "The v3 COMMAND assistant"
assistant_name = "COMMAND Lead Gen v3"

assistant = client.beta.assistants.create(
    description=assistant_description,
    model="gpt-4-turbo",
    name=assistant_name
)
print(f"New assistant created with ID: {assistant.id}")

updated_assistant = client.beta.assistants.update(
    assistant_id=assistant.id,
    tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}}
)
print("Assistant updated with vector store!")