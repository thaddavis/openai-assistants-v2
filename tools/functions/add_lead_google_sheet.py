import gspread
import json
import os

from oauth2client.service_account import ServiceAccountCredentials


# Set up Google Sheets API credentials
def authenticate_gsheets():
    scope = "https://spreadsheets.google.com/feeds https://www.googleapis.com/auth/drive"

    # Read credentials from environment variable
    creds_json = os.getenv("GOOGLE_CREDENTIALS")
    if not creds_json:
        raise ValueError(
            "❌ GOOGLE_CREDENTIALS not found in environment variables.")

    creds_dict = json.loads(creds_json)
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)

    return client


# Append a row to a Google Spreadsheet
def add_lead_to_google_sheet(email: str, phone_number: str, notes: str):
    """
    Appends a row to a Google Sheet.

    :param spreadsheet_id: The ID of the Google Sheet (from its URL).
    :param sheet_name: The sheet/tab name (e.g., "Sheet1").
    :param row_data: A list representing a row (e.g., ["John Doe", "john@example.com", "123-456-7890"]).
    """
    client = authenticate_gsheets()
    sheet = client.open_by_key(
        "1frcV3MUEsPHePcaxjEwfbtMOv6TRTFzej9y2Mx-ia64").worksheet("Sheet1")

    sheet.append_row([email, phone_number, notes])
    print("✅ Row added successfully!")
