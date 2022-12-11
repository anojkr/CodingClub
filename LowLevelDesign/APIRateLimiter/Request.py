import time

def getCurrentEpocMilli():
    return int(time.time()) * 1000

class Request(object):
    def __init__(self, ip, deviceId):
        self.ip = ip
        self.deviceId = deviceId
        self.time = None

    def setTime(self):
        self.time = getCurrentEpocMilli()
        return self
