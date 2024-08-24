import csv
import os
import os.path
import re


# def config():
#     path = r"D:/PycharmProjects/Working-with-the-directories/data.csv"
#     return os.path.join(path)


def csv_file_exists(path):
    if os.path.exists(path):
        return True
    else:
        return False


def email_validation(email):
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(email_pattern, email) is not None:
        return True
    else:
        return False


def registration(config):
    email = input("Введите email: ")
    login = input("Придумайте логин: ")
    passwd = input("Придумайте пароль: ")
    lst_data = [email, login, passwd]
    if email_validation(email):
        if csv_file_exists(config.storage_path):
            if not check_login_exist(login, email, config):
                csv_append(lst_data, config)
                return True
            else:
                print("Такой пользователь уже существует!")
                return
        else:
            csv_create(lst_data, config)
    else:
        print("Введите корректный email!")
        return


def authorization(result_csv_read) -> bool:
    log = input("Введите логин: ")
    pas = input("Введите пароль: ")
    for item in result_csv_read:
        if item.get("Логин") == log:
            if item.get("Пароль") == pas:
                print("Вы успешно авторизовались!\n")
                return True
            else:
                print("Введен не верный пароль!\n")
                return False
        else:
            print("Такого пользователя нет!\n")
            return


def csv_create(lst: list, config):
    with open(config.storage_path, "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(lst)


def csv_append(lst: list, config):
    with open(config.storage_path, "a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(lst)


def csv_read(config) -> [dict]:
    with open(config.storage_path, "r", encoding="utf-8") as file:
        fieldnames = ["email", "Логин", "Пароль"]
        reader = csv.DictReader(file, fieldnames=fieldnames)
        row_list = []
        for row in reader:
            row_list.append(row)
        return row_list


def check_login_exist(login, email, config):
    with open(config.storage_path, 'r', encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if email == row[0] or login == row[1]:
                return True
            else:
                return False
