add_lead_to_spreadsheet_definition = {
  "type": "function",
  "function": {
    "name": "add_lead_to_spreadsheet",
    "description": "This function a business lead consisting of an email and phone number to a spreadsheet for later followup.",
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
      },
      "required": ["email", "phone_number"],
    },
  },
}