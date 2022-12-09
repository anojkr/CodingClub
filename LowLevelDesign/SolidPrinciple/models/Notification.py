from SolidPrinciple.models.NotificationType import NotificationType


class Notification(object):

    def __init__(self, message: str, notificationType: NotificationType):
        self.message = message
        self.notificationType = notificationType

    def getType(self):
        return self.notificationType

    def __str__(self):
        return "{}, {}".format(self.message, self.notificationType)
