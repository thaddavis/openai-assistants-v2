import os
import json
from tools.definitions.add_tool_definition import add_tool_definition

def create_or_load_assistant(client):
    assistant_file_path = "assistant.json"
    if os.path.exists(assistant_file_path):
        with open(assistant_file_path, "r") as file:
            assistant_data = json.load(file)
            assistant_id = assistant_data["assistant_id"]
            print(f"Loaded existing assistant ID: {assistant_id}")
    else:
        assistant = client.beta.assistants.create(
            instructions="You are a helpful assistant that can add 2 numbers using the special 'add' tool.",
            model="gpt-4-turbo",
            tools=[
                add_tool_definition
            ],
        )
        with open(assistant_file_path, "w") as file:
            json.dump({"assistant_id": assistant.id}, file)
            print(f"Created a new assistant and saved the ID: {assistant.id}")
        assistant_id = assistant.id
    return assistant_id