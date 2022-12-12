from DesingTwitter.models.ITweet import ITweet
from DesingTwitter.models.IComment import IComment
from collections import OrderedDict

class Tweet(ITweet):

    def __init__(self, tweetId, userId):
        self.tweetId = tweetId
        self.userId = userId
        self.text = ""
        self.comments = OrderedDict()

    def getUserId(self):
        return self.userId

    def getTweetId(self):
        return self.tweetId

    def getComments(self):
        return self.comments

    def addComments(self, comment: IComment):
        self.comments[comment.getCommentId()] = comment
        return self

    def delComment(self, commentId):
        return self.comments.pop(commentId)

