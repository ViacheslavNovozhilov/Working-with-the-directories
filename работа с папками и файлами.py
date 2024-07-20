import os
from pathlib import Path
from pprint import pprint

path_name = "D:\\"
start_point_path = os.path.join(path_name)


def list_content(path: str):
    return sorted(os.listdir(path))


print(f"Отправная точка диск D - {list_content(start_point_path)}\n")


def get_content_number(content):
    content_dict = {}
    content = list_content(start_point_path)
    for i in range(len(content)):
        content_dict[i] = content[i]
    return content_dict


# проверка, является ли элемент файлом, если да, то читаем
"""def is_file(lst: list):
    for elem in lst:
        if os.path.isfile(elem):
            mass = []
            with open(elem, "r", encoding="utf-8") as file:
                for line in file:
                    mass.append(line)
                    return mass


def is_dir(lst: list):
    for elem in lst:
        if os.path.isdir(elem):
            pass
"""


def choose_number(path):
    number = int(input("Введите номер файла или каталога - "))
    dict_file_dir = get_content_number(start_point_path)
    for key, value in dict_file_dir.items():
        if key == number:
            path = value + ":\\"
            new_start_point = os.path.join(path)
            pprint(get_content_number(new_start_point))


answer = input("Вы хотите просмотреть содержимое каталога? - y or n:")
if answer == "y":
    res = get_content_number(start_point_path)
    pprint(res)
    choose_number(path_name)

elif answer == "n":
    for num, elem in enumerate(list_content(start_point_path)):
        print(num, elem)
else:
    print(f"Вы должны ввести y или n !")









