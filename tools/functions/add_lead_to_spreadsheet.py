def add_lead_to_spreadsheet(email: str, phone: str):
    try:
        print(f"Calling the 'add_lead_to_spreadsheet' tool...")
        print(f"Storing lead to 'LEADS SPREADSHEET': {email} {phone}")
        print(f"Notifying sales team via email!")
        return
    except Exception as e:
        print(f"Error occurred: {e}")
        return "An error occurred while processing your request."