import threading
from collections import deque
class Topic:

    def __init__(self, topicId, topicName):
        self.topicId = topicId
        self.topicName = topicName
        self.messages = deque()
        self.subscriber = {}
        self._lock = threading.Lock()

    def getTopicId(self):
        return self.topicId

    def getTopicName(self):
        return self.topicName

    def publishMessage(self, message):
        with self._lock:
            self.messages.append(message)

    def readMessage(self, message):
        with self._lock:
            self.messages.popleft(message)

    def addSubscriber(self, subscriber):
        with self._lock:
            self.subscriber[subscriber.id] = subscriber

    def removeSubscriber(self, subscriberId):
        return self.subscriber.pop(subscriberId)

    def getAllSubscribers(self):
        return self.subscriber

    def getAllMessages(self):
        return self.messages

