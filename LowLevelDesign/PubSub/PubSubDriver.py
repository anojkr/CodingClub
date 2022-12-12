from PubSub.Queue import Queue
from PubSub.models.Message import Message
from PubSub.models.Topic import Topic
from PubSub.models.Subscriber import Subscriber
from PubSub.WorkerService import WorkerService

def pubSubDriver():

    q = Queue(WorkerService())
    q.createTopic(Topic("topicId-1", "topic_one"))
    q.createTopic(Topic("topicId-2", "topic_two"))
    q.subscriberTopic("topicId-1", Subscriber("sub-1", "sub-one"))
    q.subscriberTopic("topicId-1", Subscriber("sub-2", "sub-two"))
    q.subscriberTopic("topicId-1", Subscriber("sub-3", "sub-three"))
    q.publishMessage("topicId-1", Message("msg-1"))
    q.publishMessage("topicId-1", Message("msg-2"))
    q.publishMessage("topicId-1", Message("msg-3"))
    q.publishMessage("topicId-1", Message("msg-4"))
    q.publishMessage("topicId-1", Message("msg-5"))
    q.publishMessage("topicId-1", Message("msg-6"))
    q.publishMessage("topicId-1", Message("msg-7"))
    # q.publishMessage("topicId-2", Message("msg-3"))
    # q.getAllSubscriberByTopic("topicId-1")
    # q.getAllMessages("topicId-1")

if __name__ == "__main__":
    pubSubDriver()