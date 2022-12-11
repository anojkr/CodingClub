
from MeetingRoom.MeetingRoomsCalender import MeetingRoomsCalender
from MeetingRoom.models.ConferenceRoom import ConferenceRoom
from MeetingRoom.models.MediaRoom import MediaRoom
from MeetingRoom.UserEventService import UserEventService
from MeetingRoom.models.User import User
from MeetingRoom.models.Event import Event

def meetingRoomDriver():
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
    meetingCalender = MeetingRoomsCalender(userService)
    meetingCalender.addMeetingRoom(room1)
    meetingCalender.addMeetingRoom(room2)
    meetingCalender.getMeetingRooms()
    event1 = Event("event-1", 1203, 30, user1, room1).addGuest(user1).addGuest(user2)
    event2 = Event("event-2", 123, 12, user1, room1).addGuest(user3)
    meetingCalender.bookEvent(event1, "11-12-2022")
    meetingCalender.bookEvent(event2, "11-12-2022")
    # print(meetingCalender.getMeetingRoomById("conf_room_1").id)
    meetingCalender.getEvents("conf_room_1","11-12-2022")

if __name__ == "__main__":
    meetingRoomDriver()