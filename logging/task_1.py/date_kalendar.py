# Функция получает на вход текст вида: “1-й четверг ноября”, “3я среда мая” и.т.п.
# - Преобразуйте его в дату в текущем году.
# - Научите функцию распознавать не только текстовое названия дня недели и месяца,
# но и числовые, т.е не мая, а 5
# - При этом значение любого параметра можно опустить.
# В этом случае берётся первый в месяце день недели, текущий день недели и/или текущий месяц.
# Логируйте ошибки, если текст не соответсвует формату.

# - Добавьте возможность запуска из командной строки.
# - сраная неделя месяца

import log_kalendar
import datetime


def kalendar(date_text: str = '', day: int = 1, month: int = 1, year: int = 2023):
    if date_text == '':
        text = "Успешно преобразована дата!"
        print(text)
        log_kalendar.log_info_triangle(text)
        return datetime.date(year, month, day)
    try:
        data = datetime.datetime.strptime(date_text, '%W %A %B').replace(year=year)
        text = "Успешно преобразована дата!"
        print(text)
        log_kalendar.log_info_triangle(text)
        return data
    except ValueError:
        text = "Произошла ошибка по причине не правильно указанного формата переданных аргументов"
        print(text)
        log_kalendar.log_warning_triangle(text)