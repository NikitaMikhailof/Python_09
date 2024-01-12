'''
Задание №6
Доработайте классы исключения так, чтобы они выдали
подробную информацию об ошибках.
Передавайте необходимые данные из основного кода
проекта.
'''

import json

FILE_NAME = "users.json"


class MyException(Exception):
    pass


class LevelException(MyException):

    def __str__(self):
        return f"Нельзя создать пользователя не залогиневшись или если ваш уровень меньше"


class AccessError(MyException):
    def __init__(self, name, id_):
        self.name, self.id = name, id_

    def __str__(self):
        return f"Пользователь с id {self.id} и именем {self.name} не найден"


class User:
    def __init__(self, name: str, id_: str, level: str):
        self.name = name
        self.id = int(id_)
        self.level = int(level)

    def __str__(self):
        return f"Имя: {self.name}, id: {self.id}, level: {self.level}"

    def __eq__(self, other):
        return isinstance(other, User) and self.id == other.id and self.name == other.name

    def __hash__(self):
        return hash((self.name, self.id))


class Project:

    def __init__(self):
        self.active_user = None
        self.users = set()

    def get_users(self, file_name: str) -> set:
        with open(file_name, encoding='utf-8') as f:
            try:
                file_dict = json.load(f)
            except json.decoder.JSONDecodeError:
                file_dict = {}
            for elem in file_dict:
                self.users.add(User(elem['name'], elem['id'], elem['level']))
        return self.users

    def login(self, name: str, id_: str):
        temp_user = User(name, id_, 0)
        for user in self.users:
            if user == temp_user:
                self.active_user = user
                break
        else:
            raise AccessError(name, id_)

    def add_user(self, name, id_, level):
        if self.active_user and level >= self.active_user.level:
            new_user = User(name, id_, level)
            self.users.add(new_user)
            return new_user
        else:
            raise LevelException()


if __name__ == '__main__':
    project = Project()
    print(*project.get_users(FILE_NAME), sep="\n")
    print("-" * 10)
    project.login("John Travolta", 1214)
    print(project.active_user)
    print("-" * 10)
    print(project.add_user("Катя", 251, 5))

   