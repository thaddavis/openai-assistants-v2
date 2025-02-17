from dotenv import load_dotenv

from tools.functions.add import add
load_dotenv()
import json
import time
from helpers.create_or_load_assistant import create_or_load_assistant
from openai import OpenAI
import os

def main():
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    # Create or load assistant
    assistant_id = create_or_load_assistant(client)
    print(f"Using assistant ID: {assistant_id}")

    # Create a new thread
    thread = client.beta.threads.create()
    print(f"Thread created with ID: {thread.id}")

    # Run a loop where the user can ask questions
    while True:
        text = input("What's your question? (Type 'quit' to exit)\n")
        if text.lower() == 'quit':
            break

        # Create a user message in the thread
        user_message = client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=text
        )

        # Run the assistant to get a response
        run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant_id
        )

        # Polling for the run status
        i = 0
        while run.status not in ["completed", "failed", "requires_action"]:
            if i > 0:
                time.sleep(5)
            run = client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id
            )
            i += 1
            print(run.status)

        # Handle required actions
        if run.status == "requires_action":
            tools_to_call = run.required_action.submit_tool_outputs.tool_calls
            print(len(tools_to_call))
            print(tools_to_call)

            tool_output_array = []

            for each_tool in tools_to_call:
                tool_call_id = each_tool.id  # Correct attribute for tool_call_id
                function_name = each_tool.function.name
                function_args = json.loads(each_tool.function.arguments)  # Parse the JSON string

                print(f"Tool ID: {tool_call_id}")
                print(f"Function to call: {function_name}")
                print(f"Parameters to use: {function_args}")

                # Call the perplexity_search function directly
                if function_name == "add":
                    output = add(function_args['a'], function_args['b'])
                else: 
                    output = "Invalid function name"

                tool_output_array.append({"tool_call_id": tool_call_id, "output": output})

            print(tool_output_array)

            # Submit the tool outputs
            run = client.beta.threads.runs.submit_tool_outputs(
                thread_id=thread.id,
                run_id=run.id,
                tool_outputs=tool_output_array
            )

            # Check the run operation status again
            i = 0
            while run.status not in ["completed", "failed", "requires_action"]:
                if i > 0:
                    time.sleep(10)
                run = client.beta.threads.runs.retrieve(
                    thread_id=thread.id,
                    run_id=run.id
                )
                i += 1
                print(run.status)

        # Retrieve the assistant's response message
        response_message = None
        messages = client.beta.threads.messages.list(thread_id=thread.id).data
        for message in messages:
            if message.role == "assistant":
                response_message = message
                break

        if response_message:
            print(f"Assistant response: {response_message.content}\n")
        else:
            print("No assistant response found.\n")

if __name__ == "__main__":
    main()