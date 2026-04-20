import unittest

from models.book import Book
from models.user import Student
from services.factory import NotificationFactory
from services.library import Library
from services.notification import EmailNotification, SMSNotification


class TestLibrarySystem(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book = Book(1, "1984", "George Orwell")
        self.user1 = Student(1, "Aldas")
        self.user2 = Student(2, "Jonas")

        self.library.add_book(self.book)
        self.library.add_user(self.user1)
        self.library.add_user(self.user2)

    def test_borrow_book(self):
        self.library.borrow_book(1, 1)
        self.assertFalse(self.book.is_available())

    def test_return_book(self):
        self.library.borrow_book(1, 1)
        self.library.return_book(1)
        self.assertTrue(self.book.is_available())

    def test_reserve_book_when_unavailable(self):
        self.library.borrow_book(1, 1)
        self.library.reserve_book(2, 1)
        self.assertEqual(len(self.library._reservations), 1)

    def test_reserve_book_when_available(self):
        self.library.reserve_book(2, 1)
        self.assertEqual(len(self.library._reservations), 0)

    def test_factory_creates_email_notification(self):
        notification = NotificationFactory.create_notification("email")
        self.assertIsInstance(notification, EmailNotification)

    def test_factory_creates_sms_notification(self):
        notification = NotificationFactory.create_notification("sms")
        self.assertIsInstance(notification, SMSNotification)

    def test_factory_invalid_type(self):
        with self.assertRaises(ValueError):
            NotificationFactory.create_notification("push")


if __name__ == "__main__":
    unittest.main()