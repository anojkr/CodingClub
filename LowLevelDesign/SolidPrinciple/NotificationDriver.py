
from SolidPrinciple.NotificationService import NotificationService
from SolidPrinciple.models.Notification import Notification
from SolidPrinciple.models.NotificationType import NotificationType
from SolidPrinciple.NotificationServiceFactory import NotificationServiceFactory

def notificationDriver():
    notificationService = NotificationService(NotificationServiceFactory())
    notificationService.sendNotification(Notification("email", NotificationType.EMAIL))
    notificationService.sendNotification(Notification("sms", NotificationType.SMS))


if __name__ == '__main__':
    notificationDriver()