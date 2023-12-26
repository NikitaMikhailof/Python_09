from  random import sample, randint 

'''
Напишите функцию, которая генерирует 
псевдоимена. 
✔ Имя должно начинаться с заглавной буквы, 
состоять из 4-7 букв, среди которых 
обязательно должны быть гласные. 
✔ Полученные имена сохраните в файл
'''

def generation_pseudo_name(name_file: str, count_name: int)-> str:
    LIST_LETTERS = [chr(i) for i in range(97, 123)]
    LIST_VOWEL_LETTERS =  ['a', 'e', 'i', 'o', 'u', 'y']
    for _ in range(count_name):
        COUNT_LETTERS = randint(4, 7)
        with open(f'{name_file}.csv', 'a+', encoding='utf-8') as f:
            flag = True
            while flag:
                word = ''.join(sample(LIST_LETTERS, COUNT_LETTERS))
                if len(list(filter(lambda x: x in LIST_VOWEL_LETTERS, word))) >= 1:
                    flag = False
            f.write(f'{word.capitalize()}\n')        


if __name__ == '__main__':
    generation_pseudo_name('pseudo_names', 15)


