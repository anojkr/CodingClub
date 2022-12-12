

from DesingTwitter.models.User import User
from DesingTwitter.UserService import UserService
from DesingTwitter.models.Tweet import Tweet
from DesingTwitter.TwittterService import TwitterService

def twitterDriver():
    user1 = User("user-1", "user-1")
    user2 = User("user-2", "user-2")
    user3 = User("user-3", "user-3")
    user4 = User("user-4", "user-4")
    userService = UserService()
    twitterService = TwitterService(userService)
    userService.addUser(user1)
    userService.addUser(user2)
    userService.addUser(user3)
    userService.addUser(user4)
    userService.addFollowee(user2, "user-1")
    userService.addFollowee(user3, "user-1")
    userService.addFollowee(user4, "user-1")
    user1.getFollowees()
    tweet1 = Tweet("tweet-1", "user-2")
    tweet2 = Tweet("tweet-2", "user-3")
    tweet3 = Tweet("tweet-4", "user-4")
    twitterService.postTweet(tweet1)
    twitterService.postTweet(tweet2)
    twitterService.postTweet(tweet3)

    twitterService.getUserFeed("user-1")

if __name__ == "__main__":
    twitterDriver()