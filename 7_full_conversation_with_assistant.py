import time
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

assistant_id = "asst_8XaMCZ0jXistHLFdTEi2HKfo"

vector_store_id = "vs_67b290c49ed08191876522f0882b837a"

# Update the assistant with the vector store ID in the tool_resources
my_updated_assistant = client.beta.assistants.update(
    assistant_id=assistant_id,
    instructions="You are a helpful assistant.",
    name="AI Assistant",
    tools=[{"type": "file_search"}],  # Enable file search
    tool_resources={"file_search": {"vector_store_ids": [vector_store_id]}},
)
print("Assistant Updated:", my_updated_assistant)

# Create a new thread
thread = client.beta.threads.create()
print(f"Thread created with ID: {thread.id}")

# Run a loop where user can ask questions
while True:
    text = input("What's your question? (Type 'quit' to exit)\n")
    if text.lower() == 'quit':
        break

    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=text,
    )
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant_id
    )

    # Retrieve the assistant's response message
    response_message = None
    messages = client.beta.threads.messages.list(thread_id=thread.id).data

    for message in messages:
        if message.role == "assistant" and message.created_at > run.created_at:
            response_message = message
            break

    if response_message:
        print(f"Assistant response: {response_message.content}\n")
    else:
        print("No assistant response found.\n")