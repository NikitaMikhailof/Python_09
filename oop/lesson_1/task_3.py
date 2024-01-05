'''
Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.
'''

class InformationHuman:
    
    def __init__(self, name, surname, age):
        self.name = name  
        self.surname = surname
        self.__age = age 

    def birthday(self):    
        self.__age += 1 

    def full_name(self):
        return f'{self.name} {self.surname}'  

    def age_info(self):
        return self.__age     

if __name__ == '__main__':   
    i = InformationHuman('Sasha', 'Goryachev', 25)   
    print(i._InformationHuman__age)
    i.birthday()
    print(i.full_name(), i._InformationHuman__age)  