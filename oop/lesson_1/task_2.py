'''
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.
'''

class Rectangle:

    def __init__(self, lenght, width=None): 
        self.lenght = lenght
        self.width = width 
        if self.width == None:
            self.width = self.lenght = lenght

    def perimeter(self):
        return (self.lenght + self.width) * 2
        
    def square(self):
        return self.lenght * self.width  
    

if __name__ == '__main__':
    r1 = Rectangle(10, 5)
    r2 = Rectangle(10) 
    print(f'Периметр фигуры равен = {r1.perimeter()}\nПлощадь фигуры равна = {r1.square()}\n')
    print(f'Периметр фигуры равен = {r2.perimeter()}\nПлощадь фигуры равна = {r2.square()}')     