import os
import shutil
import datetime
from random import randint


def system_info(message):
    """Write a message about the action and it's time in the file 'log.txt'."""
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(f'{datetime.datetime.now()} - {message}\n')


def choose_path(new_path):
    """Changes the directory"""
    try:
        os.chdir(new_path)
    except FileNotFoundError:
        print('Выбранный путь не существует.\n')
    else:
        print('Путь изменен.\n')


def available_directories():
    """Shows a list of directories in the current one."""
    result = [item for item in os.listdir() if os.path.isdir(item)]
    print(result, end='\n\n') if result else print('Вложенных папок нет.\n')


def show_content():
    """Shows contents of the current directory."""
    result = os.listdir()
    print(result, end='\n\n') if result else print('Текущая папка пуста.\n')


def go_back():
    """For coming back to general directory."""
    old_path = os.getcwd()
    os.chdir('../')
    new_path = os.getcwd()
    print(os.getcwd(), end='\n\n') if old_path != new_path else print('Вы находитесь в корневой папке.\n')


def create_folder(name):
    """Create folder in chosen directory or in the current one."""
    try:
        os.mkdir(name)
    except FileNotFoundError:
        print('Системе не удается найти указанный путь.\n')
    except FileExistsError:
        print('Невозможно создать файл, так как он уже существует.\n')
    except OSError:
        print('Синтаксическая ошибка в имени файла, имени папки или метке тома.\n')
    else:
        print('Папка создана.\n')


def create_file(name, text=None):
    """Create a file in chosen directory or in the current one."""
    try:
        if os.path.exists(name):
            raise FileExistsError
        with open(name, 'w', encoding='utf-8') as f:
            if text:
                f.write(text)
    except FileExistsError:
        print('Невозможно создать файл, так как он уже существует.\n')
    except FileNotFoundError:
        print('Системе не удается найти указанный путь.\n')
    except OSError:
        print('Синтаксическая ошибка в имени файла, имени папки или метке тома.\n')
    else:
        print('Файл создан.\n')


def delete(name):
    """Delete folder or file in chosen directory or in the current one."""
    try:
        os.rmdir(name) if os.path.isdir(name) else os.remove(name)
    except FileNotFoundError:
        print('Не удается найти указанный путь.\n')
    except OSError:
        print('Папка не пуста. Все равно удалить?(y/n)')
        answer = input('>>> ')
        while not (answer == 'y' or answer == 'n'):
            print('Неизвестная команда.')
            answer = input('Вы хотите удалить вложенные папки и файлы?(y/n)\n>>> ')
        if answer == 'y':
            shutil.rmtree(name)
            print('Удалено.\n')
        else:
            print('Не удалено.\n')
    else:
        print('Удалено.\n')


def copy(name, new_name):
    """Copy folder or file in chosen directory or in the current one."""
    isdir = os.path.isdir(name)
    try:
        shutil.copytree(name, new_name) if isdir else shutil.copy(name, new_name)
    except FileExistsError:
        print(f'Невозможно создать {"папку" if isdir else "файл"}, так как он{"a" if isdir else ""} уже существует.\n')
    except FileNotFoundError:
        print('Не удается найти указанный путь.\n')
    except OSError:
        print('Синтаксическая ошибка в имени файла, имени папки или метке тома.\n')
    else:
        print('Скопировано.\n')


def play_game():
    """Start the game with your computer."""
    print('Игра начинается.\n')

    input('Загадайте число от 0 до 100, но не говорите мне. Загадали? (Нажмите Enter)\n>>> ')
    response = None
    minimum = 0
    maximum = 100
    count = 0

    while response != 'ура!':
        count += 1
        try:
            new_attempt = randint(minimum, maximum)
        except ValueError:
            print('Похоже, Вы нарушаете правила...\nЯ так не играю!\n')
            break
        print(f'Я думаю, Вы загадали число {new_attempt}.')
        response = input('Каков Ваш вердикт? (Загаданное число больше/меньше/ура!)\n>>> ')
        if response == 'больше':
            minimum = new_attempt + 1
        elif response == 'меньше':
            maximum = new_attempt - 1
    else:
        print('Урааа! Я тоже очень рад, что угадал!')
        if count > 5:
            print(f'Правда, мне понадобилось много попыток! Целых {count}.')
            print('Сложная задачка!\n')
        else:
            print('Легко!\n')


def help():
    print(
        'choose_path новый_путь                                -> Изменить рабочую директорию\n'
        'available_directories                                 -> Просмотр списка доступных директорий.\n'
        'show_content                                          -> Просмотр содержимого рабочей папки.\n'
        'go_back                                               -> На уровень выше.\n'
        'create_folder имя_папки                               -> Создать папку.\n'
        'create_file имя_файла                                 -> Создать файл.\n'
        'delete имя_файла_или_папки                            -> Удалить.\n'
        'copy имя_файла_или_папки имя_нового_файла_или_папки   -> Копировать.\n'
        'play_game                                             -> Сыграть в игру.\n'
        'help                                                  -> Справка.\n'
    )


if __name__ == '__main__':
    print('Тестирование.\n')

    # choose_path('C:/Users/anyta/')
    # print(f'Изменили путь: {os.getcwd()}\n')
    # available_directories()
    # show_content()

    # go_back()
    # go_back()
    # go_back()
    # go_back()
    # go_back()
    # go_back()
    # create_folder('Папка')
    # create_file('new_file.txt', 'Здравствуйте!\nМеня зовут Тимофеева Анна.')
    # delete('new_file.txt')
    # delete('Папка')

    # create_folder('Folder1')
    # choose_path('Folder1')
    # create_folder('Folder2')
    # create_file('File2.txt', '2 lvl')
    # choose_path('Folder2')
    # create_file('File3.txt', '3 lvl')

    # create_file('tema.txt', 'text text text')
    # delete('tema.txt')
    # create_folder('Folder4')
    # delete('Folder4')

    # create_folder('Folder5')
    # choose_path('Folder5')
    # create_file('File6')
    # go_back()
    # delete('Folder5')

    # create_folder('Folder6')
    # choose_path('Folder6')
    # create_file('File6')
    # go_back()
    # copy('Folder6', 'Folder7')
    # copy('Folder10', 'Folder11')
    # create_folder('Folder8')
    # copy('Folder6', 'Folder8')
    # delete('Folder8')
    # delete('Folder6')
    # delete('Folder7')

    # create_file('my_file1.txt', 'some text for my file #1')
    # copy('my_file1.txt', 'my_file2.txt')
    # delete('my_file1.txt')
    # delete('my_file2.txt')

    # system_info('test')

    # play_game()

    help()