'''
Напишите функцию, которая открывает на чтение созданные 
в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните 
имя и произведение:
✔ если результат умножения отрицательный, сохраните имя 
записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя 
прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк, 
сколько в более длинном файле. 
✔ При достижении конца более короткого файла, 
возвращайтесь в его начало.
'''

def mult_func(name_file: str)-> str:    
    with ( 
        open('digits.txt', 'r', encoding='utf-8') as f1,
        open('pseudo_names.csv', 'r', encoding='utf-8') as f2,
        open(f'{name_file}.txt', 'a+', encoding='utf-8') as f3
    ):
        file_1 = f1.readlines()
        file_2 = f2.readlines()
        max_len = max(len(file_1), len(file_2))

        for i in range(max_len):
            pseudo_name = (f'{file_2[i % len(file_1)][:-1]}')
            value_1_file_1, value_2_file_1 = file_1[i % len(file_1)].split('|')
            multiplication = round(int(value_1_file_1) * float(value_2_file_1), 3)
            if multiplication < 0:
                f3.write(f'{pseudo_name.lower()} ')
                f3.write(f'{abs(multiplication)}\n')
            else:
                f3.write(f'{pseudo_name.upper()} ')
                f3.write(f'{round(multiplication)}\n')


if __name__ == '__main__':
    mult_func('multiplication')




