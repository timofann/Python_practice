import json
import pickle

# 02: Создать модуль deserialize.py. В этом модуле открыть файлы group.json и group.pickle, прочитать из них
# информацию. И получить объект: словарь из предыдущего задания.


print('01. Десериализация словаря.', end='\n\n')

# чтение json
with open('group.json', 'r', encoding='utf-8') as f:
    my_json = json.load(f)
print(f'Json-file: {my_json}\nПроверка типа: {type(my_json)}\n')

# чтение байтов
with open('group.pickle', 'rb') as f:
    my_pickle = pickle.load(f)
print(f'Pickle-file: {my_pickle}\nПроверка типа: {type(my_pickle)}\n')
