from random import randint

'''Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функцию угадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами
из диапазонов.'''

def decoration(func):
    def wrapper(arg_1, arg_2, *args, **kwargs):
        if  1 <= arg_1 <= 100 and 1 <= arg_2 <= 10:
            res = func(arg_1, arg_2)
        else:
            res = func(randint(1, 100), randint(1, 10))  
        return res    
              
    return wrapper  


@decoration
def number_of_attempts(arg_1, arg_2):
    for i in range(arg_2):
        temp = int(input('Введите число: '))
        if temp == arg_1:
            print(f'Поздравляем вы угадали чиcло, затрачено попыток {i + 1}') 
            print(f'Загаданное число {arg_1}')
            return arg_1
    return f'Попытки закончились! Загаданное число : {temp}'
    

result = number_of_attempts(1, 5)