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

