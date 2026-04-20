class Reservation:
    def __init__(self, user, book):
        self._user = user
        self._book = book

    def get_user(self):
        return self._user

    def get_book(self):
        return self._book

    def __str__(self):
        return f"{self._user.get_name()} reserved {self._book.get_title()}"