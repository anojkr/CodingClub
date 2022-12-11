from MeetingRoom.models.User import User
from MeetingRoom.models.MeetingRoom import MeetingRoom
from datetime import datetime

class Event(object):

    def __init__(self, id, eventTime, duration, organiser, meetingRoom):
        self.id = id
        self.description = None
        self.eventTime = eventTime
        self.duration = duration
        self.organiser = organiser
        self.meetingRoom = meetingRoom
        self.guestList = []

    def getId(self):
        return self.id

    def getOrganiser(self):
        return self.organiser

    def getMeetingDuration(self):
        return self.duration

    def getGuestList(self):
        return self.guestList

    def getMeetingRoomInfo(self):
        return self.meetingRoom

    def addGuest(self, guest: User):
        self.guestList.append(guest)
        return self

    def setMeetingDuration(self, duration):
        self.duration = duration
        return self

    def setMeetingRoom(self, meetingRoom: MeetingRoom):
        self.meetingRoom = meetingRoom
        return self

    def __str__(self):
        return "\nId: {}\n\tDescription:{}\n\tEvent-time: {}\n\tDuration: {} Min".format(self.id,self.description,datetime.fromtimestamp(self.eventTime), self.duration)