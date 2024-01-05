from math import pi

'''
Создайте класс окружность.
Класс должен принимать радиус окружности при создании
экземпляра.
У класса должно быть два метода, возвращающие длину
окружности и её площадь.
'''

class Circle:

    def __init__(self, radius: int):
        self.radius = radius 

    def lenght_circle(self):
        return 2 * pi * self.radius

    def square_circle(self):
        return pi * (self.radius**2)
    
if __name__ == '__main__':
    c1 = Circle(5)
    print(c1.lenght_circle(),  c1.square_circle(), sep = '\n')




