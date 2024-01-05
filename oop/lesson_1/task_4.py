from task_3 import InformationHuman

'''
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
шестизначный идентификационный номер
уровень доступа вычисляемый как остаток от деления
суммы цифр id на семь
'''

class Employee(InformationHuman): 
    class_id = 1_000_000

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.id = self.class_id
        self.age = age
        Employee.class_id += 1 


    def access_level(self):
        return sum(map(int, str(self.id))) % 7
        
    def __str__(self):
        return  f'{self.name} {self.surname} - {self.age} old {self.id} id access key : {self.access_level()}'    


if __name__ == '__main__':
    e = Employee( 'Nikita', 'Mikhailov', 31) 
    e1 = Employee( 'Marta', 'Mikhailova', 32) 
    e2 = Employee( 'Mark', 'Mikhailov', 2) 
    print(e, e1, e2, sep = '\n')
   