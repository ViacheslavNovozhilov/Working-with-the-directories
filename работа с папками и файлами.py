import csv
import re


def registration():
    email = input("Введите email: ")
    login = input("Придумайте логин: ")
    passwd = input("Придумайте пароль: ")
    lst_data = [email, login, passwd]
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(email_pattern, email) is not None:
        csv_create(lst_data)
        check_login_exist(login, email)
    else:
        print("Введите корректный email!")


def authorization(result):
    log = input("Введите логин: ")
    pas = input("Введите пароль: ")
    for item in result:
        if item.get("Логин") == log:
            if item.get("Пароль") == pas:
                print("Вы успешно авторизовались!")
                return
            else:
                print("Введен не верный пароль!")
                return
        else:
            print("Такого пользователя нет!")


def csv_create(lst: list):
    with open("data.csv", "a", newline='', encoding="utf-8") as file:
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


def check_login_exist(login, email):
    with open('data.csv', 'r', encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if login == row[1] or email == row[0]:
                print("Пользователь с таким логином или email уже существует.")
                return


answer = int(input("Введите 1, если хотите войти\nВведите 2, если хотите зарегистрироваться"))

match answer:
    case 1:
        authorization(csv_read())
    case 2:
        registration()
    case _:
        print("Не верный ввод!")
