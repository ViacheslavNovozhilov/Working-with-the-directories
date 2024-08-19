from CSV_logic import authorization, registration, csv_read, csv_append


def start():
    answer = int(input("Введите 1, если хотите войти\nВведите 2, если хотите зарегистрироваться\n"))

    match answer:
        case 1:
            authorization(csv_read())
        case 2:
            registration()
        case _:
            print("Не верный ввод!")
