
from DistributedPubSub.Queue import Queue
from DistributedPubSub.Topic import Topic
from DistributedPubSub.Subscriber import Subscriber
from DistributedPubSub.Message import Message

def driver():
    q = Queue()
    q.createTopic(Topic("topicId-1", "topic_one"))
    q.createTopic(Topic("topicId-2", "topic_two"))
    q.subscriberTopic("topicId-1", Subscriber("sub-1", "sub-one"))
    q.subscriberTopic("topicId-1", Subscriber("sub-2", "sub-two"))
    q.subscriberTopic("topicId-1", Subscriber("sub-3", "sub-three"))
    q.publishMessage("topicId-1", Message("msg-1", "msg-1-topic-1"))
    q.getAllSubscribers("topicId-1")
    q.getAllMessages("topicId-1")


if __name__ == "__main__":
    driver()