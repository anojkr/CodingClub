from SolidPrinciple.models.Notification import Notification

class NotificationService(object):

    def __init__(self, notificationFactoryObj):
        self.notificationFactoryObj = notificationFactoryObj

    def sendNotification(self, notification: Notification):
        self.notificationFactoryObj.getNotificationProvider(notification.getType()).sendNotification(notification)
