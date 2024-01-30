# Функция получает на вход текст вида: “1-й четверг ноября”, “3я среда мая” и.т.п.
# - Преобразуйте его в дату в текущем году.
# - Логируйте ошибки, если текст не соответсвует формату.
# - Добавьте возможность запуска из командной строки.
# - При этом значение любого параметра можно опустить.
# В этом случае берётся первый в месяце день недели,
# текущий день недели и/или текущий месяц.
# - Научите функцию распознавать не только текстовое названия дня недели и месяца,
# но и числовые, т.е не мая, а 5


import argparse
from date_kalendar import kalendar

text = '13333 Thursdayfdgdf Novembetytrr'
text2 = '2 Monday May'
kalendar()
kalendar(date_text=text2)
kalendar(date_text=text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='triangle')
    parser.add_argument('param', nargs='*', help='Enter a path(s) to directory(s) to list')
    args = parser.parse_args()
    print(kalendar(*args.param))