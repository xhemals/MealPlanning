from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]

calID = "275cd9345234789bda45211612dd83a2bce5809f544b14b62b47ce7c9d87b1f8@group.calendar.google.com"


def creds():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("creds/token.json"):
        creds = Credentials.from_authorized_user_file("creds/token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "creds/credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("creds/token.json", "w") as token:
            token.write(creds.to_json())
    return creds


def runCalendar(day, meal, who):
    try:
        service = build("calendar", "v3", credentials=creds())
        mealTitle = meal
        mealStart = datetime.time(18)
        mealEnd = datetime.time(18, 30)
        start = day.combine(day, mealStart)
        end = day.combine(day, mealEnd)
        startFormatted = start.isoformat() + "Z"
        endFormatted = end.isoformat() + "Z"
        event = {
            "summary": f"{who} - {mealTitle}",
            "start": {"dateTime": startFormatted, "timeZone": "Europe/London"},
            "end": {
                "dateTime": endFormatted,
                "timeZone": "Europe/London",
            },
        }

        event = (
            service.events()
            .insert(
                calendarId=calID,
                body=event,
            )
            .execute()
        )
        print("Event created: %s" % (event.get("htmlLink")))
    except HttpError as error:
        print("An error occurred: %s" % error)


def viewEvent():
    try:
        today = datetime.date.today()
        today = datetime.datetime.combine(
            today, datetime.time(hour=0, minute=0, second=1)
        )
        startDate = today.isoformat() + "Z"
        service = build("calendar", "v3", credentials=creds())
        events_result = (
            service.events().list(calendarId=calID, timeMin=startDate).execute()
        )
        events = events_result.get("items", [])
        sorted_events = sorted(events, key=lambda x: x["start"]["dateTime"])
        eventDi = {}
        for event in sorted_events:
            dateTime = event["start"]["dateTime"].replace("Z", "").replace("T", " ")
            eventDi.update({dateTime: {}})
            eventDi[dateTime].update(
                {
                    "date": f"{dateTime}",
                    "meal": f'{event["summary"]}',
                    "eventID": f'{event["id"]}',
                }
            )
        return eventDi

    except HttpError as error:
        print("An error occurred: %s" % error)


def furthestEvent():
    try:
        service = build("calendar", "v3", credentials=creds())
        today = datetime.date.today()
        today = datetime.datetime.combine(
            today, datetime.time(hour=0, minute=0, second=1)
        )
        startDate = today.isoformat() + "Z"
        events_result = (
            service.events().list(calendarId=calID, timeMin=startDate).execute()
        )
        events = events_result.get("items", [])
        sorted_events = sorted(
            events, key=lambda x: x["start"]["dateTime"], reverse=True
        )
        eventDi = {}
        for event in sorted_events:
            dateTime = event["start"]["dateTime"].replace("Z", "").replace("T", " ")
            eventDi.update({dateTime: {}})
            eventDi[dateTime].update(
                {
                    "date": f"{dateTime}",
                    "meal": f'{event["summary"]}',
                }
            )
        firstEntry = next(iter(eventDi))
        return firstEntry

    except HttpError as error:
        print("An error occurred: %s" % error)


def editEvent(meal, who, eventID):
    try:
        service = build("calendar", "v3", credentials=creds())
        event = service.events().get(calendarId=calID, eventId=eventID).execute()
        event["summary"] = f"{who} - {meal}"
        service.events().update(calendarId=calID, eventId=eventID, body=event).execute()
    except HttpError as error:
        print("An error occurred: %s" % error)
