import os
from pathlib import Path
from pprint import pprint

path_name = r'D:\\'
point_path = os.path.join(path_name)


def list_content(path: str):
    return sorted(os.listdir(path))


lst = list_content(point_path)
print(f"Отправная точка диск D - {list_content(point_path)}\n")


def get_content_number(lst_content):
    content_dict = {}
    for i in range(len(lst_content)):
        content_dict[i] = lst_content[i]
    return content_dict


pprint(get_content_number(lst))


def choose_number(num):
    lst_res = list_content(point_path)
    dict_file_dir = get_content_number(lst_res)
    for key, value in dict_file_dir.items():
        new_start_point = os.path.join(point_path, value)
        if num == key:
            if os.path.isfile(new_start_point):
                with open(new_start_point, "r", encoding="utf-8") as file:
                    while True:
                        line = file.readline()
                        if not line:
                            break
                        print(line.strip())
            else:
                res = list_content(new_start_point)
                return get_content_number(res)


def question(answer):
    if answer == "y":
        get_file_dir_number(int(input("Введите номер файла или каталога - ")))
    elif answer == "n":
        for num, elem in enumerate(list_content(point_path)):
            print(num, elem)
    else:
        print(f"Вы должны ввести y или n !")


def get_file_dir_number(number):
    res = choose_number(number)
    pprint(res)


question(input("Хотите посмотреть содержимое каталога? - "))
