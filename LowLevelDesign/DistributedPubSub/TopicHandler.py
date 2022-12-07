class TopicHandler:

    def __init__(self, topic):
        self.topic = topic

    def publishMessage(self, message):
        self.topic.addMessage(message)

    def addSubscribe(self, subscriber):
        self.topic.addSubscriber(subscriber)

    def getAllMessages(self):
        return self.topic.getAllMessages()

    def getAllSubscribers(self):
        return self.topic.getAllSubscribers()

