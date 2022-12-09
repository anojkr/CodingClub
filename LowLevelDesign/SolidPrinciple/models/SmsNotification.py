from SolidPrinciple.models.NoticationInterface import NotificationInterface
from SolidPrinciple.models.Notification import Notification


class SmsNotification(NotificationInterface):

    def sendNotification(self, notification: Notification):
        print("Send Sms notification: {}".format(notification))
