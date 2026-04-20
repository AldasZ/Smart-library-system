from models.book import Book
from models.user import User
from models.reservation import Reservation
from services.factory import NotificationFactory


class Library:
    def __init__(self):
        self._books = []
        self._users = []
        self._reservations = []

    def add_book(self, book: Book):
        self._books.append(book)

    def add_user(self, user: User):
        self._users.append(user)
    
    def get_books(self):
        return self._books

    def get_users(self):
        return self._users

    def show_books(self):
        for book in self._books:
            print(book)

    def borrow_book(self, user_id: int, book_id: int):
        book = self._find_book(book_id)
        user = self._find_user(user_id)

        if not book or not user:
            print("User or book not found")
            return

        if book.borrow():
            print(f"{user.get_name()} borrowed {book.get_title()}")
        else:
            print("Book is not available")

    def return_book(self, book_id: int):
        book = self._find_book(book_id)

        if not book:
            print("Book not found")
            return

        book.return_book()
        print(f"{book.get_title()} returned")
        self._check_reservations(book)

    def reserve_book(self, user_id: int, book_id: int):
        book = self._find_book(book_id)
        user = self._find_user(user_id)

        if not book or not user:
            print("User or book not found")
            return

        if book.is_available():
            print("Book is available, no need to reserve")
        else:
            reservation = Reservation(user, book)
            self._reservations.append(reservation)
            print(f"{user.get_name()} reserved {book.get_title()}")

    def _find_book(self, book_id: int):
        for book in self._books:
            if book.get_id() == book_id:
                return book
        return None

    def _find_user(self, user_id: int):
        for user in self._users:
            if user.get_id() == user_id:
                return user
        return None

    def _check_reservations(self, book: Book):
        for reservation in self._reservations:
            if reservation.get_book() == book:
                user = reservation.get_user()

                notification = NotificationFactory.create_notification("email")
                notification.send(
                    user.get_name(),
                    f"The book '{book.get_title()}' is now available."
                )

                self._reservations.remove(reservation)
                break