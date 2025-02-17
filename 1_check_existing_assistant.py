from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
assistant_id: str = "asst_DRhqZDYmVN48m1486qDDY6jF"
my_assistant = client.beta.assistants.retrieve(assistant_id=assistant_id)
print("Assistant Details: ", my_assistant)
