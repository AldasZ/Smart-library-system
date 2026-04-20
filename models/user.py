class User:
    def __init__(self, user_id: int, name: str):
        self._user_id = user_id
        self._name = name

    def get_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def __str__(self):
        return self._name
    
class Student(User):
    def __init__(self, user_id: int, name: str):
        super().__init__(user_id, name)


class Librarian(User):
    def __init__(self, user_id: int, name: str):
        super().__init__(user_id, name)