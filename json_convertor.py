import os
import sys
import json
from progress.bar import IncrementalBar  # отслеживаем прогресс выполнения скрипта


def custom_filename(data):
    filename = str(input("Введите название файла и расширение .json, для конвертации нажмите Enter.\n"))

    bar = IncrementalBar('Processing', max = len(data))

    with open(filename, "w", encoding="utf-8") as json_file:
        for chunk in json.JSONEncoder(ensure_ascii=False, indent=4).iterencode(data):
            bar.next()  # запускаем прогрессбар
            json_file.write(chunk)
        bar.finish()  # завершаем отслеживание прогресса


# Читаем файл
def reading_file_and_create_tuple():
    data = []

    while True:
        try:
            source_path = str(input("Введите путь до файла: "))

            # проверяем существует ли введенный адрес и файл
            if os.path.exists(source_path):
                # существует ли файл
                if os.path.isfile(source_path):
                    print(":------***------:")
                    print("Файл: ", source_path)
                    print(":------***------:")
                    print("Размер: ", os.path.getsize(source_path) // 1024, "Кб")
                    print(":------***------:")

                # октроем файл для чтения если такой существует
                source_filepath = open(source_path, "rt", encoding="utf-8")
                # если файл существует, запишем строки из файла, в кортеж
                bar = IncrementalBar('Processing', max = len(data))
                for string in source_filepath:
                    bar.next()
                    string = string.rstrip()  # убираем последний символ '\n' из s
                    data = data + [string]  # добавляем строку в список
                bar.finish()

                # проверяем содержимое кортежа и выводим информацию в консоль
                if len(data) > 0:
                    source_name = source_path
                    print("Содержимое файла", source_name, "успешно записаны в кортеж.\n", "Количество строк в кортеже  - ", len(data))
                    print(":------***------:")
                    custom_name = custom_filename(data)  # Вызывваем функцию нейминга файла и генератора json
                    print(":------***------:")
                else:
                    print("None")
                sys.exit()
            else:
                print("Неправильный путь, повторите попытку снова")


        except OSError as e:
            print(e.errno)


def input_state():
    # Hello, @username@
    message_hello = "Введите имя файла, который необходимо конвертировать из txt в json: "
    # бесконечный цикл, который продолжает выполняться
    # до возникновения исключения
    while True:
        try:
            contin_mod = 1
            exit_mod = 2

            hello_world = "Чтобы продолжить введите 1, чтобы выйти введите 2: "

            start_prog = int(input(hello_world))  # int() Задаём тип вводимых знаков, а именно числовые
            user_value = start_prog

            if user_value == contin_mod:
                file_path = reading_file_and_create_tuple()
            elif user_value == exit_mod:
                sys.exit()  # выход из программы


        except ValueError:
            # цикл будет повторяться до правильного ввода
            error_txt = "Ошибка! Это не число, попробуйте снова."
            print(error_txt)
        else:
            break

input_state()



