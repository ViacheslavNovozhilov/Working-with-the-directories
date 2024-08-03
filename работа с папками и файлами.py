import csv
import re
#клон для гита


def registration():
    email = input("Введите email: ")
    login = input("Придумайте логин: ")
    passwd = input("Придумайте пароль: ")
    lst_data = [email, login, passwd]
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(email_pattern, email) is not None:
        csv_create(lst_data)
    else:
        print("Введите корректный email!")


def authorization(result):
    log = input("Введите логин: ")
    pas = input("Введите пароль: ")
    for item in result:
        if item.get("Логин") == log:
            if item.get("Пароль") == pas:
                print("Вы успешно авторизовались!")
            else:
                print("Введен не верный пароль!")
        else:
            print("Такого пользователя нет!")


def csv_create(lst: list):
    with open("data.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(lst)


def csv_read() -> [dict]:
    with open("data.csv", "r", encoding="utf-8") as file:
        fieldnames = ["email", "Логин", "Пароль"]
        reader = csv.DictReader(file, fieldnames=fieldnames)
        row_list = []
        for row in reader:
            row_list.append(row)
        return row_list


answer = int(input("Введите 1, если хотите войти\nВведите 2, если хотите зарегистрироваться"))

match answer:
    case 1:
        authorization(csv_read())
    case 2:
        registration()
    case _:
        print("Не верный ввод!")
