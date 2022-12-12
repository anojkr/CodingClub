import threading

from PubSub.IQueue import IQueue
from PubSub.models.ITopic import ITopic

class Queue(IQueue):
    TopicMap = None

    def __init__(self, workerService):
        self.__class__.TopicMap = {}
        self.workerService = workerService
        self._lock = threading.Lock()

    def getTopicById(self, topicId):
        return self.__class__.TopicMap.get(topicId)

    def createTopic(self, topic: ITopic):
        with self._lock:
            self.__class__.TopicMap[topic.getTopicId()] = topic
            return self

    def deleteTopic(self, topicId):
        return self.__class__.TopicMap.pop(topicId)

    def subscriberTopic(self, topicId, subscriber):
        self.__class__.TopicMap.get(topicId).addSubscriber(subscriber)
        return self

    def unsubscribeTopic(self, topicId, subscriberId):
        return self.__class__.TopicMap.get(topicId).pop(subscriberId)

    def publishMessage(self, topicId, message):
        with self._lock:
            topic = self.__class__.TopicMap.get(topicId)
            topic.publishMessage(message)
            self.workerService.consumeMessage(topic)

    def getAllSubscriberByTopic(self, topicId):
        subscribers = self.__class__.TopicMap.get(topicId).getTopicSubscribers()
        subscriberIds = [_.getSubscriberId() for _ in subscribers]
        print("Subscriber = [{}] has subscribed to topic: {}".format(",".join(map(str, subscriberIds)), topicId))
        return subscribers

    def getAllMessages(self, topicId):
        messages = self.__class__.TopicMap.get(topicId).getAllMessages()
        print("Messages: [{}] for topic: {}".format(",".join(map(str, messages)), topicId))
        return messages
