from DesingTwitter.models.User import User
from DesingTwitter.models.IUser import IUser


class UserService(object):
    UserMap = {}

    def __init__(self):
        self.__class__.UserMap = {}

    def getUser(self, userId):
        return self.__class__.UserMap.get(userId)

    def addUser(self, user: IUser):
        self.__class__.UserMap[user.getUserId()] = user
        return self

    def delUser(self, userId):
        return self.__class__.UserMap.pop(userId)

    def addFollower(self, user: IUser, userId):
        self.__class__.UserMap.get(userId).addFollower(user)

    def addFollowee(self, user: IUser, userId):
        self.__class__.UserMap.get(userId).addFollowee(user)


