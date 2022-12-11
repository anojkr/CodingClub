
from MeetingRoom.MeetingRoomsCalender import MeetingRoomsCalender
from MeetingRoom.models.ConferenceRoom import ConferenceRoom
from MeetingRoom.models.MediaRoom import MediaRoom
from MeetingRoom.UserEventService import UserEventService
from MeetingRoom.models.User import User
from MeetingRoom.models.Event import Event
from MeetingRoom.LinearBookEvent import LinearBookEvent
from datetime import datetime

def meetingRoomDriver():
    bookStrategy = LinearBookEvent()
    userService = UserEventService()
    user1 = User("user-1")
    user2 = User("user-2")
    user3 = User("user-3")
    userService.addUser(user1)
    userService.addUser(user2)
    userService.addUser(user3)
    userService.getAllUsers()
    room1 = ConferenceRoom("conf_room_1").setCapacity(10)
    room2 = MediaRoom("media_room_1").setCapacity(5)
    meetingCalender = MeetingRoomsCalender(userService, bookStrategy)
    meetingCalender.addMeetingRoom(room1)
    meetingCalender.addMeetingRoom(room2)
    meetingCalender.getMeetingRooms()

    event_one_startTime = 1670893200
    eventOneDayEpoc = datetime.fromtimestamp(event_one_startTime).date().today().strftime('%s')

    event_two_startTime = 1670889612
    eventTwoDayEpoc = datetime.fromtimestamp(event_two_startTime).date().today().strftime('%s')

    event1 = Event("event-1", event_one_startTime, 30, user1, room1).addGuest(user2).addGuest(user1)
    event2 = Event("event-2", event_two_startTime, 59, user1, room1).addGuest(user3).addGuest(user1)
    meetingCalender.bookEvent(event1, eventOneDayEpoc)
    meetingCalender.bookEvent(event2, eventTwoDayEpoc)
    meetingCalender.getEvents("conf_room_1", eventTwoDayEpoc)
    userService.getUserEvent("user-1",eventTwoDayEpoc)

if __name__ == "__main__":
    meetingRoomDriver()