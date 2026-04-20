class Book:
    def __init__(self, book_id: int, title: str, author: str):
        self._book_id = book_id
        self._title = title
        self._author = author
        self._is_available = True

    # Getteriai (Encapsulation)
    def get_id(self):
        return self._book_id

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def is_available(self):
        return self._is_available

    # Logika
    def borrow(self):
        if self._is_available:
            self._is_available = False
            return True
        return False

    def return_book(self):
        self._is_available = True

    def __str__(self):
        status = "Available" if self._is_available else "Borrowed"
        return f"{self._title} by {self._author} [{status}]"