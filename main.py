from models.book import Book
from models.user import Student
from models.reservation import Reservation


def main():
    book = Book(1, "1984", "George Orwell")
    user = Student(1, "Aldas")

    print(book)

    # Borrow
    book.borrow()
    print(book)

    # Reservation
    reservation = Reservation(user, book)
    print(reservation)

    # Return
    book.return_book()
    print(book)


if __name__ == "__main__":
    main()

from models.book import Book
from models.user import Student
from services.library import Library


def main():
    library = Library()

    # Add data
    book1 = Book(1, "1984", "George Orwell")
    user1 = Student(1, "Aldas")

    library.add_book(book1)
    library.add_user(user1)

    # Test
    library.show_books()

    library.borrow_book(1, 1)
    library.show_books()

    library.return_book(1)

    library.reserve_book(1, 1)


if __name__ == "__main__":
    main()