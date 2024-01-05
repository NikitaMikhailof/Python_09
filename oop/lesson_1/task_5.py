'''
Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.
'''

class Fish:
    
    def __init__(self, name, max_dept):
        self.name = name
        self.max_dept = max_dept
    
    def spec(self):
        return self.max_dept 
       

class Bird:

    def __init__(self, name, wingspan):
        self.name = name 
        self.wingspan = wingspan

    def spec(self):
        return self.wingspan    


class Cat:

    def __init__(self, name, jump_heigth):
       self.name = name  
       self.jump_heigth = jump_heigth 

    def spec(self):
        return self.jump_heigth 
    

if __name__ == '__main__':
    f = Fish('fugo', 100)    
    b = Bird('parrot', 30) 
    c = Cat('Barsik', 160)
    print(f.spec(), b.spec(), c.spec(), sep = '\n')

