from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os
import pickle

SCOPES = ["https://www.googleapis.com/auth/contacts"]

def get_service():
    creds = None

    if os.path.exists("token.pkl"):
        with open("token.pkl", "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
        )
        creds = flow.run_local_server(port=0, prompt='consent')

        with open("token.pkl", "wb") as token:
                pickle.dump(creds, token)

    service = build("people", "v1", credentials=creds)
    return service



def create_contact(service, name, phone, note):
    contact_body = {
        "names": [{"givenName": name}],
        "phoneNumbers": [{"value": phone}],
        "biographies": [{"value": note}]
    }
    service.people().createContact(body=contact_body).execute()