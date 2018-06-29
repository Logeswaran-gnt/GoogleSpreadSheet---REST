from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('sheets', 'v4', http=creds.authorize(Http()))

SPREADSHEET_ID = '1CCEffLl3iojlwhuC0QSxTiYelssMNFfFEbKCHlWgSbQ'
RANGE_NAME = 'CONSOLIDATED!A1:B'

request = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME)
response = request.execute()

print(response)