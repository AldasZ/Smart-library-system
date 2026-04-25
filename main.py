from models.book import Book
from models.user import Student
from services.library import Library
from utils.file_handler import FileHandler


def print_menu():
    print("\n--- Library Menu ---")
    print("1. Show books")
    print("2. Add book")
    print("3. Add user")
    print("4. Borrow book")
    print("5. Return book")
    print("6. Reserve book")
    print("7. Save data")
    print("8. Load data")
    print("0. Exit")


def main():
    library = Library()

    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            library.show_books()

        elif choice == "2":
            book_id = int(input("Book ID: "))
            title = input("Title: ")
            author = input("Author: ")
            library.add_book(Book(book_id, title, author))

        elif choice == "3":
            user_id = int(input("User ID: "))
            name = input("Name: ")
            library.add_user(Student(user_id, name))

        elif choice == "4":
            user_id = int(input("User ID: "))
            book_id = int(input("Book ID: "))
            library.borrow_book(user_id, book_id)

        elif choice == "5":
            book_id = int(input("Book ID: "))
            library.return_book(book_id)

        elif choice == "6":
            user_id = int(input("User ID: "))
            book_id = int(input("Book ID: "))
            library.reserve_book(user_id, book_id)

        elif choice == "7":
            FileHandler.save_books("data/books.csv", library.get_books())
            FileHandler.save_users("data/users.csv", library.get_users())
            print("Data saved.")

        elif choice == "8":
            books = FileHandler.load_books("data/books.csv")
            users = FileHandler.load_users("data/users.csv")

            for b in books:
                library.add_book(b)

            for u in users:
                library.add_user(u)

            print("Data loaded.")

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()