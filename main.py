from models.book import Book
from models.user import Student, Librarian
from services.library import Library
from utils.file_handler import FileHandler


def main():
    library = Library()

    book1 = Book(1, "1984", "George Orwell")
    book2 = Book(2, "The Hobbit", "J. R. R. Tolkien")

    user1 = Student(1, "Aldas")
    user2 = Librarian(2, "Monika")

    library.add_book(book1)
    library.add_book(book2)

    library.add_user(user1)
    library.add_user(user2)

    FileHandler.save_books("data/books.csv", library.get_books())
    FileHandler.save_users("data/users.csv", library.get_users())

    loaded_books = FileHandler.load_books("data/books.csv")
    loaded_users = FileHandler.load_users("data/users.csv")

    print("Loaded books:")
    for book in loaded_books:
        print(book)

    print("\nLoaded users:")
    for user in loaded_users:
        print(user)


if __name__ == "__main__":
    main()