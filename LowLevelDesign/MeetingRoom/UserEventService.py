from MeetingRoom.models.Event import Event


class UserEventService(object):
    UserEvent = {}
    User = {}

    def __init__(self):
        self.__class__.UserEvent = {}
        self.__class__.User = {}

    def addUserEvent(self, userId, event: Event, day):
        userEvents = self.__class__.UserEvent
        if userId in self.__class__.User:
            if day not in userEvents[userId]:
                userEvents[userId][day] = []
            self.__class__.UserEvent[userId][day].append(event)
        else:
            raise BaseException("Non-existing user")

    def getAllUsers(self):
        userList = list(self.__class__.User.keys())
        print(", ".join(map(str,userList)))
        return userList

    def getUserEvent(self, userId, day):
        return self.__class__.UserEvent.get(userId).get(day)

    def addUser(self, user: User):
        self.__class__.User[user.id] = user
        self.__class__.UserEvent[user.id] = {}
        return self

    def removeUser(self, userId):
        return self.__class__.User.pop(userId)
