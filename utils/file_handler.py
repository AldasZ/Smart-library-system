import csv

from models.book import Book
from models.user import Student, Librarian


class FileHandler:
    @staticmethod
    def save_books(filename: str, books: list):
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["book_id", "title", "author", "is_available"])

            for book in books:
                writer.writerow([
                    book.get_id(),
                    book.get_title(),
                    book.get_author(),
                    book.is_available()
                ])

    @staticmethod
    def load_books(filename: str):
        books = []

        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                book = Book(
                    int(row["book_id"]),
                    row["title"],
                    row["author"]
                )

                if row["is_available"] == "False":
                    book.borrow()

                books.append(book)

        return books

    @staticmethod
    def save_users(filename: str, users: list):
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["user_id", "name", "role"])

            for user in users:
                role = user.__class__.__name__
                writer.writerow([
                    user.get_id(),
                    user.get_name(),
                    role
                ])

    @staticmethod
    def load_users(filename: str):
        users = []

        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["role"] == "Student":
                    user = Student(int(row["user_id"]), row["name"])
                elif row["role"] == "Librarian":
                    user = Librarian(int(row["user_id"]), row["name"])
                else:
                    continue

                users.append(user)

        return users