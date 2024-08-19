from CSV_logic import authorization, registration, csv_read, csv_file_exists, file_path


def start():
    answer = int(input("""Введите 1, если хотите войти
Введите 2, если хотите зарегистрироваться
Введите 3, если хотите просмотреть данные\n"""))

    match answer:
        case 1:
            authorization(csv_read())
        case 2:
            registration()
        case 3:
            print("Для просмотра пользователей необходимо ввести пароль администратора!")
            admin_passwd = "12345"
            if csv_file_exists(file_path):
                request = input("Введите пароль администратора: ")
                if request == admin_passwd:
                    result = csv_read()
                    for item in result:
                        print(item)
            else:
                print("Данных нет!")

        case _:
            print("Не верный ввод!")
