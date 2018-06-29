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

body = {
  "requests": [
    {
      "addSheet": {
        "properties": {
          "sheetId": 1,
          "title": "Lok",
          "index": 0
        }
      }
    }
  ]
}

SPREADSHEET_ID = '1CYX80r3mw5EBNWmhXINjJkRzYSk6nuqEejWSFGpL7n8'
# RANGE_NAME = 'CONSOLIDATED!A1:B'
spreadsheet_body = {

    'sheets':[{'properties':{'title':'gggggg'}},{'properties':{'title':'lllll'}}]
}
request = service.spreadsheets().batchUpdate(spreadsheetId=SPREADSHEET_ID,
                                               body=body).execute()