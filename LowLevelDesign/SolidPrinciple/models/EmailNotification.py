from SolidPrinciple.models.NoticationInterface import NotificationInterface
from SolidPrinciple.models.Notification import Notification


class EmailNotification(NotificationInterface):

    def sendNotification(self, notification: Notification):
        print("Send Email notification: {}".format(notification))
