from PubSub.models.ISubscriber import ISubscriber

class Subscriber(ISubscriber):

    def __init__(self, subscriberId, subscriberName):
        self.subscriberId = subscriberId
        self.subscriberName = subscriberName

    def getSubscriberId(self):
        return self.subscriberId

    def __str__(self):
        return "{}".format(self.subscriberId)

