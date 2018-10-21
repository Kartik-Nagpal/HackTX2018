from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import webbrowser

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar'
class CalendarPush:
    def __init__(self, Tests):
        print()


        store = file.Storage('backend/token.json')
        creds = store.get()
        

        if not creds or creds.invalid:
          flags = tools.argparser.parse_args(args=[])
          flow = client.flow_from_clientsecrets('backend/CalCred.json', SCOPES)
          creds = tools.run_flow(flow, store, flags)

        service = build('calendar', 'v3', http=creds.authorize(Http()))

        #Open URL


        # Call the Calendar API
        for eventObject in Tests:
            event = {
              'summary': str("Test for " + eventObject.getClass()),
              'description': str(eventObject.getDescription()),
              'start': {
                "date": str(eventObject.getDate()),
              },
              'end': {
                'date': str(eventObject.getDate()),
              },
              'reminders': {
                'useDefault': False,
                'overrides': [
                  {'method': 'email', 'minutes': 24 * 60},
                  {'method': 'popup', 'minutes': 10},
                ],
              },
            }
            # print(event)


            event = service.events().insert(calendarId='primary', body=event).execute()


            print ('Event created: %s' % (event.get('htmlLink')))
