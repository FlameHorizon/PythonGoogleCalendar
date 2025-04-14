import datetime
import os.path
import json
from models import Event, EventDate

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/calendar"]


def main():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("calendar", "v3", credentials=creds)

        event = Event(
            summary="Google I/O 2015",
            location="800 Howard St., San Francisco, CA 94103",
            description="A chance to hear more about Google's developer products.",
            start=EventDate(date="2020-05-28"),
            end=EventDate(date="2020-05-29"),
        )

        payload = event.to_dict()
        response = service.events().insert(calendarId='primary', body=payload).execute()

        print('Event created: %s' % (response.get('htmlLink')))

    except HttpError as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    main()
