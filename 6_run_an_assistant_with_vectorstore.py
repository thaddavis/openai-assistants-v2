import time
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

assistant_id = "asst_8XaMCZ0jXistHLFdTEi2HKfo"
vector_store_id = "vs_67b290c49ed08191876522f0882b837a"

my_updated_assistant = client.beta.assistants.update(
    assistant_id=assistant_id,
    instructions="You are an assistant specialized in qualifying and generating leads for COMMAND LABS - a software laboratory.",
    name="COMMAND Assistant v23",
    tools=[{"type": "file_search"}],  # Enable file search
    tool_resources={"file_search": {"vector_store_ids": [vector_store_id]}},
)
print("Assistant updated:", my_updated_assistant)

# Create a new thread
thread = client.beta.threads.create()
print(f"Thread created with ID: {thread.id}")

user_prompt = "Tell me about the pricing offered by COMMAND Labs."

# Create a user message in the thread
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=user_prompt
)

# vvv TECHNIQUE 1: "Create and Poll" Method vvv
# run = client.beta.threads.runs.create_and_poll(
#     thread_id=thread.id,
#     assistant_id=assistant_id,
# )
# print(f"Run completed with ID: {run.id}")
# ^^^ TECHNIQUE 1: "Create and Poll" Method vvv

# vvv TECHNIQUE 2: "Create and Check Status" Method vvv
run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=assistant_id)
print(f"Run Created: {run.id}")
while run.status != "completed":
    run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
    print(f"Run Status: {run.status}")
    time.sleep(0.5)
if run.status == "completed":
    print(f"Run Completed!")
# ^^^ TECHNIQUE 2: "Create and Check Status" Method ^^^

# Retrieve the assistant's response message
response_message = None
messages = client.beta.threads.messages.list(thread_id=thread.id).data

for message in messages:
    if message.role == "assistant":
        response_message = message
        break

if response_message:
    print(f"Assistant response: {response_message.content}")
else:
    print("No assistant response found.")