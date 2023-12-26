from  random import randint, uniform

'''
Напишите функцию, которая заполняет файл 
(добавляет в конец) случайными парами чисел. 
✔ Первое число int, второе - float разделены вертикальной чертой. 
✔ Минимальное число - -1000, максимальное - +1000. 
✔ Количество строк и имя файла передаются как аргументы функции. 
'''

LIMITS_LOW = -1000
LIMITS_HIGH = 1000


def fill_file(count_string: int, name_file: str )->str:
    for _ in range(count_string):
        first_num = randint(LIMITS_LOW, LIMITS_HIGH)
        second_num = uniform(LIMITS_LOW, LIMITS_HIGH)
        with open(f'{name_file}.txt', 'a+', encoding='utf-8') as f:
            f.write(f'{first_num}|{round(second_num, 5)}\n')

if __name__ == '__main__':
    fill_file(10, 'digits')
    