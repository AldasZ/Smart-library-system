from services.notification import EmailNotification, SMSNotification


class NotificationFactory:
    @staticmethod
    def create_notification(notification_type: str):
        if notification_type == "email":
            return EmailNotification()
        if notification_type == "sms":
            return SMSNotification()
        raise ValueError("Invalid notification type")