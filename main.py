from google import readsheet
from google import writesheet
from tachi import readtachi
import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def auth():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            with open("google\client-secret-location.txt", "r") as file:
                location = file.readline().rstrip('\n')
            file.close()
            flow = InstalledAppFlow.from_client_secrets_file(
                location, SCOPES
            )
            creds = flow.run_local_server(port=0)
    
    with open('token.json', 'w') as token:
        token.write(creds.to_json())
    
    service = build('sheets', 'v4', credentials=creds)
    return service

if __name__ == '__main__':
    service = auth()
    player_dict = readsheet.read(service)
    #writesheet.write(service)
    readtachi.read(player_dict)