from models.book import Book
from models.user import Student
from services.library import Library


def main():
    library = Library()

    book1 = Book(1, "1984", "George Orwell")
    user1 = Student(1, "Aldas")
    user2 = Student(2, "Jonas")

    library.add_book(book1)
    library.add_user(user1)
    library.add_user(user2)

    library.show_books()
    print()

    library.borrow_book(1, 1)
    print()

    library.reserve_book(2, 1)
    print()

    library.return_book(1)
    print()

    library.show_books()


if __name__ == "__main__":
    main()