import sys
from manager_lib import system_info, choose_path, available_directories, show_content, go_back, create_folder, \
    create_file, copy, delete, play_game, help

try:
    command = sys.argv[1]
except IndexError:
    command = None

if command == 'choose_path':
    try:
        choose_path(sys.argv[2])
    except IndexError:
        print('choose_path новый_путь:\n>>> Вы не указали директорию для изменения рабочего каталога.\n')
    else:
        system_info('Изменена рабочая директория.')

elif command == 'available_directories':
    available_directories()
    system_info('Просмотр доступных директорий.')

elif command == 'show_content':
    show_content()
    system_info('Просмотр содержимого папки.')

elif command == 'go_back':
    go_back()
    system_info('Изменена рабочая директория.')

elif command == 'create_folder':
    try:
        create_folder(sys.argv[2])
    except IndexError:
        print('create_folder имя_папки:\n>>> Вы не указали имя папки.')
    else:
        system_info('Создание новой папки.')
elif command == 'create_file':
    try:
        name = sys.argv[2]
    except IndexError:
        print('create_file имя_файла текст:\n>>> Вы не указали имя файла.')
    else:
        system_info('Создание нового файла.')
        try:
            text = sys.argv[3]
        except IndexError:
            create_file(name)
        else:
            create_file(name, text)

elif command == 'copy':
    try:
        name = sys.argv[2]
    except IndexError:
        print('copy имя_файла_или_папки имя_нового_файла_или_папки:\n>>> Вы не указали имя файла или папки.')
    else:
        system_info('Копирование.')
        try:
            copy(name, sys.argv[3])
        except IndexError:
            print('copy имя_файла_или_папки имя_нового_файла_или_папки:\n>>> Вы не указали имя нового файла или папки. '
                  f'Копирование будет произведено в папку/файл copy{name}')
            copy(name, 'copy' + name)

elif command == 'delete':
    try:
        delete(sys.argv[2])
    except IndexError:
        print('delete имя_файла_или_папки:\n>>> Вы не указали имя файла или папки.')
    else:
        system_info('Удаление.')

elif command == 'play_game':
    play_game()
    system_info('Игра.')

elif command == 'help':
    help()
    system_info('Помощь.')

else:
    print('Неизвестная команда.\nДля вызова справки введите команду help.')
    system_info('Неизвестная команда.')
  