from dotenv import load_dotenv
load_dotenv()
from tools.definitions.add_lead_to_spreadsheet_definition import add_lead_to_spreadsheet_definition
from tools.definitions.add_lead_to_google_sheet_definition import add_lead_to_google_sheet_tool_definition
from openai import OpenAI
import os

def main():
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    assistant_id: str = "asst_8XaMCZ0jXistHLFdTEi2HKfo"
    
    updated_assistant = client.beta.assistants.update(
        assistant_id=assistant_id,
        tools=[
          {"type": "file_search"},
          add_lead_to_google_sheet_tool_definition
        ],
    )
    
    print(updated_assistant)

if __name__ == "__main__":
    main()