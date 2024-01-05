'''
Доработайте задачу 5.
Вынесите общие свойства и методы классов в класс
Животное.
Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки.
''' 

class Animal:

    def __init__(self, name):
        self.name = name 

    def is_animal(self):
        return 'This animal'
    
    def eat(self):
        return f'{self.name} is eating'
    

class Fish(Animal):

    def __init__(self, name, max_dept):
        super().__init__(name)
        self.max_dept = max_dept
    
    def spec(self):
        return self.max_dept 
       

class Bird(Animal):

    def __init__(self, name, wingspan):
        super().__init__(name) 
        self.wingspan = wingspan

    def spec(self):
        return self.wingspan    


class Cat(Animal):

    def __init__(self, name, jump_heigth):
       super().__init__(name) 
       self.jump_heigth = jump_heigth 

    def spec(self):
        return self.jump_heigth     


if __name__ == '__main__':
    fish = Fish('Tuna', 100)
    bird = Bird('Eagle', 150)
    cat = Cat('Murka', 130) 
    print(fish.eat())