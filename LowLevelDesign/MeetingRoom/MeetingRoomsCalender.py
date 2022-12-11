import threading
from collections import defaultdict
from MeetingRoom.models.Event import Event
from MeetingRoom.models.MeetingRoom import MeetingRoom

class MeetingRoomsCalender(object):

    def __init__(self, userService):
        self.meetingRooms = {}
        self.meetingRoomMap = defaultdict(dict)
        self.userService = userService
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
            eventIds = [_.id for _ in dayEvents]
            print("All event for {} for day {} are {}".format(meetingRoomId, day, ",".join(map(str, eventIds))))
            return dayEvents
        return []

    def bookEvent(self, event: Event, day):
        meetingRoomId = event.meetingRoom.id
        with self._lock:
            if meetingRoomId in self.meetingRooms:
                if day not in self.meetingRoomMap[meetingRoomId]:
                    self.meetingRoomMap[meetingRoomId][day] = []
                self.meetingRoomMap[meetingRoomId][day].append(event)
                for guestUsr in event.guestList:
                    self.userService.addUserEvent(guestUsr.id, event, day)
            else:
                raise BaseException("Meeting Room Don't Exist")



