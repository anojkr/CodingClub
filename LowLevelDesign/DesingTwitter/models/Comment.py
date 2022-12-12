from DesingTwitter.models.IComment import IComment

class Comment(IComment):

    def __init__(self, commentId, text, userId, tweetId):
        self.commentId = commentId
        self.text = text
        self.userId = userId
        self.tweetId = tweetId

    def getTweetId(self):
        return self.tweetId

    def getUserId(self):
        return self.userId

    def getCommentId(self):
        return self.commentId