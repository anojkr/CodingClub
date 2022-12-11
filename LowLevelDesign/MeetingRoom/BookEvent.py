import abc
from MeetingRoom.models.Event import Event

class BookEvent(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def bookEvent(self, event: Event, meetingRoomMap, roomId, day):
        pass
