# 01: Создайте модуль №1 (модуль - программа на Python, т.е. файл с расширением .py). В нем создайте функцию создающую
# директории от dir_1 до dir_9 в папке из которой запущен данный код. Затем создайте вторую функцию удаляющую эти папки.
# Проверьте работу функций в этом же модуле.

import os


def create_folders(directory):
    for i in range(1, 10):
        new_path = os.path.join(directory, f'dir_{i}')
        if os.path.exists(new_path):
            print('Директории уже существуют.')
        else:
            os.mkdir(new_path)
            print(f'Создана новая папка: {new_path}')


def delete_folders(directory):
    for i in range(1, 10):
        new_path = os.path.join(directory, f'dir_{i}')
        if os.path.exists(new_path):
            os.rmdir(new_path)
            print(f'Папка удалена: {new_path}')
        else:
            print('Нет директорий для удаления.')


if __name__ == '__main__':
    current_dir = os.getcwd()
    create_folders(current_dir)
    delete_folders(current_dir)
