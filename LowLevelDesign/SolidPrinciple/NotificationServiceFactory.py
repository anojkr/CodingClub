from SolidPrinciple.models.NotificationType import NotificationType
from SolidPrinciple.models.EmailNotification import EmailNotification
from SolidPrinciple.models.SmsNotification import SmsNotification


class NotificationServiceFactory(object):
    factoryMap = {}

    def __init__(self):
        self.__class__.factoryMap = {
            NotificationType.EMAIL: EmailNotification(),
            NotificationType.SMS: SmsNotification()
        }

    def getNotificationProvider(self, notificationType: NotificationType):
        return self.__class__.factoryMap.get(notificationType)
