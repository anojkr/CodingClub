import threading
from collections import deque
from PubSub.models.ITopic import ITopic
from PubSub.models.IMessage import IMessage
from PubSub.models.ISubscriber import ISubscriber

class Topic(ITopic):

    def __init__(self, topicId, topicName):
        self.topicId = topicId
        self.topicName = topicName
        self.subscribers = {}
        self._lock = threading.Lock()
        self.messages = deque()

    def getTopicId(self):
        return self.topicId

    def getTopicSubscribers(self):
        return self.subscribers.values()

    def getSubscriberById(self, subscriberId):
        return self.subscribers.get(subscriberId)

    def addSubscriber(self, subscriber: ISubscriber):
        self.subscribers[subscriber.getSubscriberId()] = subscriber

    def publishMessage(self, message: IMessage):
        print("Message: {} add to {} Queue".format(self.topicId, message.getMessageId()))
        self.messages.append(message)

    def getAllMessages(self):
        return self.messages

