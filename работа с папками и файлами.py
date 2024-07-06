import os
from pathlib import Path

path_name = "D:\\"
start_point_path = os.path.join(path_name)
list_content = os.listdir(start_point_path)
print(f"Отправная точка {path_name}")
print(sorted(list_content), "\n")


def is_file(lst: list):
    for elem in lst:
        if os.path.isfile(elem):
            with open(elem, "r", encoding="utf-8") as file:
                file.read()


def content_get_number(lst: list):
    content_dict = {}
    for i in range(len(lst)):
        content_dict[i] = lst[i]
    return content_dict


def show_content(content):
    if isinstance(content, dict):
        print(content)
    else:
        is_file(content)


def question():
    answer = input("Вы хотите просмотреть содержимое каталога? - y or n:")
    if answer == "y":
        show_content(content_get_number(list_content))
    elif answer == "n":
        pass
    else:
        print(f"Вы должны ввести y или n !")


question()




