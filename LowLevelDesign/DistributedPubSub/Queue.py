from DistributedPubSub.TopicHandler import TopicHandler
from DistributedPubSub.Message import Message
from DistributedPubSub.Subscriber import Subscriber
from DistributedPubSub.Topic import Topic

class Queue:

    topicMap = {}

    def __init__(self):
        self.__class__.topicMap = {}

    def createTopic(self, topic: Topic):
        self.__class__.topicMap[topic.topicId] = TopicHandler(topic)
        print("Topic with id:{} is created".format(topic.topicId))

    def deleteTopic(self, topicId: str):
        self.__class__.topicMap.pop(topicId)
        print("Topic with id:{} is deleted".format(topicId))

    def publishMessage(self, topicId, message: Message):
        self.topicMap.get(topicId).publishMessage(message)
        print("Message: {} is published to {}".format(message.id, topicId))

    def addSubscriber(self, topicId:str, subscriber: Subscriber):
        self.topicMap.get(topicId).addSubscribe(subscriber)
        print("Subscriber: {} is added to {}".format(subscriber.id, topicId))

    def getAllSubscribers(self, topicId):
        allSubscribers = self.topicMap.get(topicId).getAllSubscribers()
        print("Subscribers of {} are {}".format(topicId, list(allSubscribers.keys())))
        return allSubscribers

    def getAllMessages(self, topicId):
        allMessages = self.topicMap.get(topicId).getAllMessages()
        print("Messages of {} are {}".format(topicId, map(str, allMessages.id)))
        return allMessages
