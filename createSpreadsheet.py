from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

SCOPES = 'https://www.googleapis.com/auth/drive'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)

service = build('sheets', 'v4', credentials=creds)

spreadsheet_body = {
    'properties':{'title':'googleSpreadSheet'},
    # 'sheets':[{'properties':{'title':'logeswaran'}},{'properties':{'title':'guna'}}]
}

request = service.spreadsheets().create(body=spreadsheet_body)
response = request.execute()