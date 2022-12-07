from DistributedPubSub.Message import Message

class Subscriber:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def consumeMessage(self, message: Message):
        print("Message {} is consumed by {}".format(message.id, self.id))
