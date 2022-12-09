"""

    JobScheduler

    Requirement
    1. Create/Delete Job
    2. Query all job owned by user
    3. Query status of job by Id
    4. Get execution history
    5. Retry support
    6. On-time execution

    Traffic Estimation
    1. One million active user

    Database:
    1. NoSql/Sql don't matter
    2. Operation would be read heavy
    3. We need to have distribute workers to run job concurrently

    HLD (createdAt, updatedAt)
    User(userId, email)
    Job(jobId, userId,  interval)
    JobHistory(jobId, executionId,  status[Failed, Running, Completed], workerId, retryCount)
    ScheduleTable(nextExecutionTime, jobId)

    select * from ScheduleTable where  nextExecutionTime >= 1641082500 nextExecutionTime < 1641082580

    API
    createJob(userId)
    deleteJob(jobId, userId)
    getAllJobForUserId(userId)
    internalApi -> addExecutionHistory(jobId)
    internalApi -> updateNextExecutionTime(jobId)
    internalApi -> getAllJobToRun()

    Architecture

    WebService, Database,  SchedulingService, ExecutionService

    Handling Failure By HealthCheck -> Update updatedAT localDb every 10 sec and  health check will check
    for stale update and do  retry on it by  pushing it to queue


"""

class Subscriber:

  def __init__(self, id, name):
    self.id = id
    self.name = name

  def consume(self):
    print("Msg conumed by {}".format(self.id))


class PublishManager:
  eventMap = {}
  def ___int__(self):
    self.eventMap = {}


  def addEvent(self,event):
    self.eventMap[event] = []

  def getAllEvent(self):
    print(self.eventMap)

  def pushlish(self, event):
    eventExist = self.eventMap.get(event)
    if eventExist:
        for sub in eventExist:
          sub.consume()

  def subscriberEvent(self, event, subscriber):
        if event in self.eventMap:
            self.eventMap[event].append(subscriber)

  def unscriberEvent(self, event, subId):
        index = -1
        if event in self.eventMap:
            subList = self.eventMap.get(event)
            for i in range(0, len(subList)):
              if subList[i].id== subId:
                index = i
        if index!=-1:
          subList.pop(index)
        print("event unsubscribe")

pb = PublishManager()
pb.addEvent("event1")
sub1 = Subscriber("sub1", "subsciber-one")
sub2 = Subscriber("sub2", "subsciber-two")
pb.subscriberEvent("event1", sub1)
pb.subscriberEvent("event1", sub2)
pb.getAllEvent()
pb.pushlish("event1")
# pb.pushlish("event1")
# pb.pushlish("event1")
# pb.pushlish("event1")
pb.unscriberEvent("event1", "sub1")
print("\n Test")
pb.pushlish("event1")
# pb.getAllEvent()
