from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, user_name: str, message: str):
        pass


class EmailNotification(Notification):
    def send(self, user_name: str, message: str):
        print(f"Email sent to {user_name}: {message}")


class SMSNotification(Notification):
    def send(self, user_name: str, message: str):
        print(f"SMS sent to {user_name}: {message}")