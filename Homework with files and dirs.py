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


def is_file_check(point):
    if os.path.isfile(point):
        return True


def is_dir_check(point):
    if os.path.isdir(point):
        return True


def recieve_content_by_chosen_number(num):
    lst_res = list_content(point_path)
    dict_file_dir = get_content_number(lst_res)
    for key, value in dict_file_dir.items():
        new_start_point = os.path.join(point_path, value)
        if num == key:
            if is_file_check(new_start_point):
                with open(new_start_point, "r", encoding="utf-8") as file:
                    return [line.strip() for line in file]
            elif is_dir_check(new_start_point):
                res = list_content(new_start_point)
                return get_content_number(res)
            else:
                return


def get_file_dir_number(number):
    res = recieve_content_by_chosen_number(number)
    return res


answer = input(f"""Если вы хотите просмотреть содержимое {point_path}, нажмите Y
Если нет, то нажмите N\n""")
match answer:
    case "y":
        pprint(get_content_number(lst))
        answer1 = int(input("Введите номер файла или каталога - "))
        pprint(get_file_dir_number(answer1))
    case "n":
        print(f"Вы находитесь в {point_path}")
    case _:
        print(f"Вы должны ввести y или n !")


