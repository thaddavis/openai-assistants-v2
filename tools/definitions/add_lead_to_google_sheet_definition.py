add_lead_to_google_sheet_tool_definition = {
    "type": "function",
    "function": {
        "name": "add_lead_to_google_sheet",
        "description":
        "This function adds a business lead consisting of an email and phone number to a Google sheet for later followup.",
        "parameters": {
            "type": "object",
            "properties": {
                "email": {
                    "type": "string",
                    "description": "The email address of the lead",
                },
                "phone_number": {
                    "type": "string",
                    "description": "The phone number of the lead",
                },
                "notes": {
                    "type": "string",
                    "description": "Additional notes about the lead",
                }
            },
            "required": ["email", "phone_number", "notes"],
        },
    },
}
