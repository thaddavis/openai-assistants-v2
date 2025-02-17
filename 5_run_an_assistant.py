from dotenv import load_dotenv
load_dotenv()
import time
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
assistant_id = "asst_8XaMCZ0jXistHLFdTEi2HKfo"
user_prompt = "What is 2+2?"

print(f"PROMPT: {user_prompt}")

chat = client.beta.threads.create(
    messages=[
        {
            "role": "user",
            "content": user_prompt  # User-defined prompt
        }
    ]
)

run = client.beta.threads.runs.create(thread_id=chat.id, assistant_id=assistant_id)
print(f"Run Created: {run.id}")

while run.status != "completed":
    run = client.beta.threads.runs.retrieve(thread_id=chat.id, run_id=run.id)
    print(f"Run Status: {run.status}")
    time.sleep(0.5)

if run.status == "completed":
    print(f"Run Completed!")

message_response = client.beta.threads.messages.list(thread_id=chat.id)
messages = message_response.data

print(f"Total Messages: {len(messages)}")

if messages:    
    latest_message = messages[0]
    if latest_message.role == 'assistant':
        print(f"RESPONSE: {latest_message.content[0].text.value}")
else:
    print("No response found.")