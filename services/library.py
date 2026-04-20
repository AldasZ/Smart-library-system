from models.book import Book
from models.user import User
from models.reservation import Reservation


class Library:
    def __init__(self):
        self._books = []
        self._users = []
        self._reservations = []

    # --- BOOK MANAGEMENT ---
    def add_book(self, book: Book):
        self._books.append(book)

    def show_books(self):
        for book in self._books:
            print(book)

    # --- USER MANAGEMENT ---
    def add_user(self, user: User):
        self._users.append(user)

    # --- BORROW ---
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

    # --- RETURN ---
    def return_book(self, book_id: int):
        book = self._find_book(book_id)

        if not book:
            print("Book not found")
            return

        book.return_book()
        print(f"{book.get_title()} returned")

        # Patikrinam rezervacijas
        self._check_reservations(book)

    # --- RESERVATION ---
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

    # --- HELPERS ---
    def _find_book(self, book_id):
        for book in self._books:
            if book.get_id() == book_id:
                return book
        return None

    def _find_user(self, user_id):
        for user in self._users:
            if user.get_id() == user_id:
                return user
        return None

    def _check_reservations(self, book):
        for reservation in self._reservations:
            if reservation.get_book() == book:
                print(f"Reservation available for {reservation.get_user().get_name()}")
                self._reservations.remove(reservation)
                break