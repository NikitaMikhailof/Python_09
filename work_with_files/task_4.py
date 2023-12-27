from random import randint, sample, choice
import string
from os import mkdir



'''
Создайте функцию, которая создаёт файлы с указанным расширением. 
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.
'''


def generation_name(min_length_name = 6, max_length_name = 30):
    letters = string.ascii_letters
    count_letters = randint(min_length_name, max_length_name)
    name_file = sample(letters, count_letters)
    return ''.join(name_file).lower()



def generation_file(count_files = 42,
                    min_bytes = 256,
                    max_bytes = 4096,
                    folder = 'task_4_work_files'):
    
    list_extensions = ['txt', 'csv', 'md', 'json', 'xls', 'html']
    for _ in range(count_files):
        extension = choice(list_extensions)
        file_name = generation_name()
        try:
            write_to_file(folder, file_name,
                          extension,
                          min_bytes, max_bytes)
        except FileNotFoundError:
            mkdir(folder)
            write_to_file(folder, file_name,
                          extension,
                          min_bytes, max_bytes)
            
def write_to_file(folder,
                  file_name,
                  extension,
                  min_bytes,
                  max_bytes):
    with open(f'{folder}/{file_name}.{extension}', 'w') as file:
        data = bytes(randint(1, 255) for _ in range(randint(min_bytes, max_bytes)))
        file.write(str(data))

    

if __name__ == '__main__':
    generation_file()

    

    

