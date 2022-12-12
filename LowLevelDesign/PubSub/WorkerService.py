from PubSub.models.ITopic import ITopic


class WorkerService(object):

    def consumeMessage(self, topic: ITopic):
        messages = topic.getAllMessages()
        worker = list(topic.getTopicSubscribers())
        res = []
        for msg in messages:
            if msg.getMessageStatus() == False:
                res.append(msg)
        size = len(res)
        count = 0
        if len(res) >= 2:
            while count < size:
                msgWorker = worker[count % len(worker)]
                msg = messages[count]
                print("{} consumed by {}".format(msg, msgWorker))
                msg.setMessageStatus()
                # print("{}-{}".format(msgWorker.getMessageId(),msg))
                count += 1
