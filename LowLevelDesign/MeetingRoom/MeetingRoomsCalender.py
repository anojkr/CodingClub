import threading
from collections import defaultdict
from MeetingRoom.models.Event import Event
from MeetingRoom.models.MeetingRoom import MeetingRoom

class MeetingRoomsCalender(object):

    def __init__(self, userService, bookStrategy):
        self.meetingRooms = {}
        self.meetingRoomMap = defaultdict(dict)
        self.userService = userService
        self.bookStrategy = bookStrategy
        self._lock = threading.Lock()

    def addMeetingRoom(self, meetingRoom: MeetingRoom):
        self.meetingRooms[meetingRoom.id] = meetingRoom

    def getMeetingRooms(self):
        for id,room in self.meetingRooms.items():
            print("{}, id: {}".format(room.roomType, id))

    def getMeetingRoomById(self, roomId):
        return self.meetingRooms.get(roomId)

    def removeMeetingRoom(self, meetingRoomId):
        with self._lock:
            return self.meetingRooms.pop(meetingRoomId)

    def getEvents(self, meetingRoomId, day):
        dayEvents = self.meetingRoomMap.get(meetingRoomId).get(day)
        if dayEvents:
            for event in dayEvents:
                print(event)
            return dayEvents
        return []

    def bookEvent(self, event: Event, day):
        roomId = event.meetingRoom.id
        with self._lock:
            if roomId in self.meetingRooms:
                if day not in self.meetingRoomMap[roomId]:
                    self.meetingRoomMap[roomId][day] = []
                    self.meetingRoomMap[roomId][day].append(event)
                else:
                    self.bookStrategy.bookEvent(event, self.meetingRoomMap, roomId, day)
                    self.meetingRoomMap[roomId][day].append(event)
                for guestUsr in event.guestList:
                    self.userService.addUserEvent(guestUsr.id, event, day)
            else:
                raise BaseException("Meeting Room Don't Exist")



