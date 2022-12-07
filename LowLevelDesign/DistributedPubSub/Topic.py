
class Topic:

    def __init__(self, topicId, topicName):
        self.topicId = topicId
        self.topicName = topicName
        self.messages = []
        self.subscriber = {}

    def getTopicId(self):
        return self.topicId

    def getTopicName(self):
        return self.topicName

    def addMessage(self, message):
        self.messages.append(message)

    def addSubscriber(self, subscriber):
        self.subscriber[subscriber.id] = subscriber

    def removeSubscriber(self, subscriberId):
        return self.subscriber.pop(subscriberId)

    def getAllSubscribers(self):
        return self.subscriber

    def getAllMessages(self):
        return self.messages

