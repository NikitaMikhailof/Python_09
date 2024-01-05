import json 
import csv 
import os

def read_json_write_csv(file_name_read, file_name_write):
    with(
        open(file_name_read, 'r', encoding='utf-8') as r,
        open(file_name_write, 'w', newline='') as w
    ):
        dictionary = json.load(r)
        csv_write = csv.DictWriter(w, fieldnames= ['id', 'name', 'level'])
        csv_write.writeheader()
        for dct in dictionary:
            csv_write.writerow({'id': dct['id'], 'name': dct['name'], 'level': dct['level']})
        
        
    
if __name__ == '__main__':
    os.chdir(r"D:\Student\JSON\Python_09\json")
    read_json_write_csv('main.json', 'main.csv')

    



