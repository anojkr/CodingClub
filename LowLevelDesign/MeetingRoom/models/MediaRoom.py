from MeetingRoom.models.MeetingRoomType import MeetingRoomType
from MeetingRoom.models.MeetingRoom import MeetingRoom


class MediaRoom(MeetingRoom):

    def __init__(self, id: str):
        self.id = id
        self.roomType = MeetingRoomType.MEDIA_ROOM
        self.capacity = 20

    def getId(self):
        self.id

    def getCapacity(self):
        return self.capacity

    def setCapacity(self, capacity):
        self.capacity = capacity
        return self

    def getRoomType(self):
        return self.meetingRoomType
