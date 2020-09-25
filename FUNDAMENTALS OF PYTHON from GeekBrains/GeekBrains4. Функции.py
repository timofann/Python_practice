# 01: Создайте функцию, принимающую на вход имя, возраст и город проживания человека. Функция должна возвращать строку
# вида «Василий, 21 год(а), проживает в городе Москва»

print('01. Анкета.', end='\n\n')


def my_output(name, age, city):
    return f'{name}, {age} год(а), проживает в городе {city}'


my_name, my_age, my_city = input('Введите своё имя, возраст и город проживания: ').split(' ')
print(my_output(my_name, my_age, my_city), end='\n\n')

# 02: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

print('02. Максимальное из трех.', end='\n\n')


def max3(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


num1, num2, num3 = map(lambda num: int(num), input('Введите 3 числа: ').split())
# num1, num2, num3 = [int(num) for num in input('Введите 3 числа: ').split()]
print(max3(num1, num2, num3), end='\n\n')

# 03: Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health = 100,
# damage = 50. ### Поэкспериментируйте с значениями урона и жизней по желанию. ### Теперь надо создать функцию
# attack(person1, person2). Примечание: имена аргументов можете указать свои. ### Функция в качестве аргумента будет
# принимать атакующего и атакуемого. ### В теле функция должна получить параметр damage атакующего и отнять это
# количество от health атакуемого. Функция должна сама работать со словарями и изменять их значения.

print('03. Сражение.', end='\n\n')

player = dict(name=input('Введите Ваше имя: '), health=100, damage=50)
enemy = dict(name=input('Введите имя противника: '), health=100, damage=50)


def attack(person1, person2):
    if person2['health'] > 0:
        person2['health'] -= person1['damage']
        print(f'{person2["name"]}: -{person1["damage"]} ед., здоровье: {person2["health"]} ед.')
    if person2['health'] <= 0:
        print(f'{person2["name"]} убит.', end='\n\n')


while enemy['health'] > 0:
    if input('Введите команду [Атаковать!], когда захотите напасть: ') == 'Атаковать!':
        attack(player, enemy)

# 04: Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр - armor = 1.2 (величина брони
# персонажа)
# Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно, у вас должно быть 2 функции:
# Наносит урон. Это улучшенная версия функции из задачи 3.
# Вычисляет урон по отношению к броне.
# Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья
# персонажа.

print('04. Сражение в броне.', end='\n\n')

player = dict(name=input('Введите Ваше имя: '), health=100, damage=50, armor=1.2)
enemy = dict(name=input('Введите имя противника: '), health=100, damage=50, armor=1.2)


def attack(person1, person2, f):
    player_damage = f(person1['damage'], person2['armor'])
    if person2['health'] > 0:
        person2['health'] -= player_damage
        print(f'{person2["name"]}: -{player_damage} ед., здоровье: {person2["health"]} ед.')
    if person2['health'] <= 0:
        print(f'{person2["name"]} убит.', end='\n\n')


while enemy['health'] > 0:
    if input('Введите команду [Атаковать!], когда захотите напасть: ') == 'Атаковать!':
        attack(player, enemy, lambda damage, armor: damage/armor)
