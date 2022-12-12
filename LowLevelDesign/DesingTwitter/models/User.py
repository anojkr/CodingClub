from DesingTwitter.models.IUser import IUser
from collections import defaultdict


class User(IUser):

    def __init__(self, userId, userEmail):
        self.userId = userId
        self.userEmail = userEmail
        self.follower = defaultdict(dict)
        self.followee = defaultdict(dict)

    def getUserId(self):
        return self.userId

    def addFollower(self, user: IUser):
        self.follower[user.getUserId()] = user
        return self

    def unFollow(self, userId):
        self.follower.pop(userId)
        return self

    def getFollowers(self):
        return self.follower.values()

    def getFollowees(self):
        followees = self.followee.values()
        userFollowee = [_.userId for _ in followees]
        print(", ".join(map(str, userFollowee)))
        return followees

    def addFollowee(self, user: IUser):
        self.followee[user.getUserId()] = user

    def removeFollowee(self, userId):
        self.self.followee.pop(userId)
        return self
