import json
import pickle

# 01: Создать модуль serialize.py. В модуле определить словарь для вашей любимой музыкальной группы.
# С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал.
# Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.


print('01. Сериализация словаря.', end='\n\n')

# словарь
my_favourite_group = {
    'name': 'Gorillaz',
    'tracks': ['Stop the Dams', 'On Melancholy Hill', 'Feel Good Inc.'],
    'albums': [dict(name='D-sides', year=2007),
               dict(name='Plastic Beach', year=2010)]
}
print(f'Dictionary: {my_favourite_group}\nПроверка типа: {type(my_favourite_group)}\n')

# json
my_favourite_group_json = json.dumps(my_favourite_group)
print(f'Json: {my_favourite_group_json}\nПроверка типа: {type(my_favourite_group_json)}\n')

# pickle
my_favourite_group_pickle = pickle.dumps(my_favourite_group)
print(f'Pickle: {my_favourite_group_pickle}\nПроверка типа: {type(my_favourite_group_pickle)}\n')

# запись в файлы
with open('group.json', 'w', encoding='utf-8') as f:  # w - запись с начала файла (перезапись)
    json.dump(my_favourite_group, f)

with open('group.pickle', 'wb') as f:
    pickle.dump(my_favourite_group, f)
