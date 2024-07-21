import os
from pathlib import Path
from pprint import pprint

path_name = r'D:\\'
point_path = os.path.join(path_name)


def list_content(path: str):
    return sorted(os.listdir(path))


print(f"Отправная точка диск D - {list_content(point_path)}\n")


def get_content_number(lst_content):
    content_dict = {}
    for i in range(len(lst_content)):
        content_dict[i] = lst_content[i]
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


def choose_number(num):
    lst = list_content(point_path)
    dict_file_dir = get_content_number(lst)
    for key, value in dict_file_dir.items():
        if num == key:
            new_start_point = os.path.join(value)
            res = list_content(new_start_point)
            return get_content_number(res)


def question(answer):
    lst = list_content(point_path)
    if answer == "y":
        res = get_content_number(lst)
        pprint(res)
    elif answer == "n":
        for num, elem in enumerate(list_content(point_path)):
            print(num, elem)
    else:
        print(f"Вы должны ввести y или n !")


def get_file_dir_number(number):
    pprint(choose_number(number))


question(input("Хотите посмотреть содержимое каталога? - "))
get_file_dir_number(int(input("Введите номер файла или каталога - ")))
