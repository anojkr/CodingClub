from MeetingRoom.BookEvent import BookEvent
from MeetingRoom.models.Event import Event

def addMinutes(epoc, minutes):
    return epoc*1000 + minutes*60*1000

def toEpocMilli(epoc):
    return epoc*1000

class LinearBookEvent(BookEvent):

    def bookEvent(self, event: Event, meetingRoomMap, roomId, day):
        roomDayEvents = meetingRoomMap.get(roomId).get(day)
        eventStartTime = toEpocMilli(event.eventTime)
        eventEndTime =  addMinutes(event.eventTime, event.duration)
        for bookedEvent in roomDayEvents:
            slotStartTime = toEpocMilli(bookedEvent.eventTime)
            slotEndTime = addMinutes(bookedEvent.eventTime, bookedEvent.duration)
            if slotStartTime <= eventStartTime < slotEndTime:
                raise BaseException("Time slot already booked")
            elif slotStartTime <= eventEndTime < slotEndTime:
                raise BaseException("Time slot already booked")