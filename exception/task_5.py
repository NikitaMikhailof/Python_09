'''
Задание №5
Доработаем задачи 3 и 4. Создайте класс проекта, который
имеет следующие методы:
загрузка данных (функция из задания 4)
вход в систему - требует указать имя и id пользователя. Для
проверки наличия пользователя в множестве используйте
магический метод проверки на равенство пользователей.
Если такого пользователя нет, вызывайте исключение
доступа. А если пользователь есть, получите его уровень из
множества пользователей.
добавление пользователя. Если уровень пользователя
меньше, чем ваш уровень, вызывайте исключение уровня
доступа.
'''
import json


FILE_NAME = "users.json"


class MyException(Exception):
    pass


class LevelException(MyException):
    pass


class AccessError(MyException):
    pass


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
        temp_user = User(name, id_, 1)
        for user in self.users:
            if user == temp_user:
                self.active_user = user
                break
        else:
            raise AccessError("Пользователь не найден")

    def add_user(self, name, id_, level):
        if self.active_user and level >= self.active_user.level:
            new_user = User(name, id_, level)
            self.users.add(new_user)
            return new_user
        else:
            raise LevelException(f"Нельзя создать пользователя не залогиневшись или если ваш уровень меньше")


if __name__ == '__main__':
    project = Project()
    print(*project.get_users(FILE_NAME), sep="\n")
    print("-" * 10)
    project.login("John Travolta", 1214)
    print(project.active_user)
    print("-" * 10)
    print(project.add_user("Катя", 251, 5))