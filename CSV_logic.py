import csv
import re
import os.path
import os


file_path = r"D:/PycharmProjects/Working-with-the-directories/data.csv"


def csv_file_exists(path):
    if os.path.exists(path):
        return True
    else:
        return False


def registration():
    email = input("Введите email: ")
    login = input("Придумайте логин: ")
    passwd = input("Придумайте пароль: ")
    lst_data = [email, login, passwd]
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(email_pattern, email) is not None:
        if csv_file_exists(file_path):
            if check_login_exist(login, email) == False:
                csv_append(lst_data)
            else:
                print("Такой пользователь уже существует!")
                return
        else:
            csv_create(lst_data)
    else:
        print("Введите корректный email!")
        return 


def authorization(result_csv_read):
    log = input("Введите логин: ")
    pas = input("Введите пароль: ")
    for item in result_csv_read:
        if item.get("Логин") == log:
            if item.get("Пароль") == pas:
                print("Вы успешно авторизовались!")
                return
            else:
                print("Введен не верный пароль!")
                return
        else:
            print("Такого пользователя нет!")
            return


def csv_create(lst: list):
    with open(r"data.csv", "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(lst)


def csv_append(lst: list):
    with open(r"data.csv", "a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(lst)


def csv_read() -> [dict]:
    with open(r"data.csv", "r", encoding="utf-8") as file:
        fieldnames = ["email", "Логин", "Пароль"]
        reader = csv.DictReader(file, fieldnames=fieldnames)
        row_list = []
        for row in reader:
            row_list.append(row)
        return row_list


def check_login_exist(login, email):
    with open(r'data.csv', 'r', encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if email == row[0] or login == row[1]:
                return True
            else:
                return False
