from DistributedPubSub.Message import Message

class Subscriber:

    def __init__(self, subscriberId, name):
        self.subscriberId = subscriberId
        self.name = name

    def consumeMessage(self, message: Message):
        print("Message {} is consumed by {}".format(message.messageId, self.subscriberId))
