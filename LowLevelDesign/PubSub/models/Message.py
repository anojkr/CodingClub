from PubSub.models.IMessage import IMessage


class Message(IMessage):

    def __init__(self, messageId):
        self.readStatus = False
        self.messageId = messageId
        self.payload = None

    def getMessageId(self):
        return self.messageId

    def getMessagePayload(self):
        return self.payload

    def setMessagePayload(self, payload):
        self.payload = payload
        return self

    def setMessageStatus(self):
        self.readStatus = True
        return self

    def getMessageStatus(self):
        return self.readStatus

    def __str__(self):
        return "{}".format(self.messageId)
