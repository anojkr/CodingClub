from DesingTwitter.models.ITweet import ITweet
from DesingTwitter.models.IComment import IComment
from collections import defaultdict

class TwitterService(object):

    TweetMap = {}
    UserTweetMap = {}

    def __init__(self, userService):
        self.userService = userService
        self.__class__.TweetMap = {}
        self.__class__.UserTweetMap = defaultdict(dict)

    def postTweet(self, tweet: ITweet):
        self.__class__.TweetMap[tweet.getTweetId()] = tweet
        self.__class__.UserTweetMap[tweet.getUserId()][tweet.getTweetId()] = tweet
        return self

    def getTweet(self, tweetId):
        return self.__class__.TweetMap(tweetId)

    def getUserTweets(self, userId):
        return self.__class__.UserTweetMap(userId)

    def delTweet(self, tweetId):
        tweet = self.__class__.TweetMap.pop(tweetId)
        self.__class__.UserTweetMap.get(tweet.getUserId()).pop(tweetId)

    def getUserFeed(self, userId):
        user = self.userService.getUser(userId)
        userFollowee = user.getFollowees()
        userFeedTweet = []
        for user in userFollowee:
            followeeTweet = self.__class__.UserTweetMap.get(user.userId)
            userFeedTweet.extend(followeeTweet.keys())
        tweets = ", ".join(map(str,userFeedTweet))
        print("UserFeed for user {} are tweet [{}]".format(userId, tweets))
        return userFeedTweet
