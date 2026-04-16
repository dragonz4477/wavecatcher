import os
import google.auth
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def auth():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'C:/Users/Morgan/Documents/google_client_secret.json', SCOPES
            )
            creds = flow.run_local_server(port=0)
    
    with open('token.json', 'w') as token:
        token.write(creds.to_json())
    
    service = build('sheets', 'v4', credentials=creds)
    return service

def call(service, id, range):
    try:
        result = (
            service.spreadsheets()
            .values()
            .get(spreadsheetId=id, range=range)
            .execute()
        )

        rows = result.get("values", [])
        return rows
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error

def read():
    service = auth()
    
    with open('google\sheetinfo.txt', 'r') as info:
        lines = info.readlines()
        lines = [line.rstrip("\n") for line in lines]
        
        id = lines[1]
        name = lines[3]
        player_column = lines[5]
        rating_column = lines[7]
        rows = lines[9].split(':')
        
        start = rows[0]
        end = rows[1]

        sheet_range = f"\'{name}\'!{player_column}{start}:{rating_column}{end}"

        players = call(service, id, sheet_range)
        
        for i in range(len(players)):
            players[i] = [val for val in players[i] if val != '']
        
        player_dict = {}
        for player in players:
            player_dict[player[0]] = player[1]
        
        return player_dict