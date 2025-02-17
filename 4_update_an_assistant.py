from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

assistant_id = "asst_8XaMCZ0jXistHLFdTEi2HKfo"
new_name = "COMMAND Assistant v23"
new_description = "The new and improved COMMAND Assistant v23"

updated_assistant = client.beta.assistants.update(
    assistant_id=assistant_id,
    name=new_name,
    description=new_description,
    instructions="You are an assistant specialized in qualifying and generating leads for COMMAND LABS - a software laboratory.",
    model="gpt-4-turbo",
)
print(updated_assistant)