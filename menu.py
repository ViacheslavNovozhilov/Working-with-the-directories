from CSV_logic import authorization, registration, csv_read, csv_file_exists
from config import Config


def start():
    cfg = Config()
    while True:
        answer = int(input("""Введите 1, если хотите войти
Введите 2, если хотите зарегистрироваться
Введите 3, если хотите просмотреть данные
Введите 4, если хотите выйти\n"""))

        match answer:
            case 1:
                result = authorization(csv_read(cfg))
                if result:
                    print("Вы успешно авторизовались!\n")
                else:
                    print("Введен не верный пароль!\n")
            case 2:
                registration(cfg)
            case 3:
                print("Для просмотра пользователей необходимо ввести пароль администратора!")
                admin_passwd = "12345"
                if csv_file_exists(cfg.storage_path):
                    request = input("Введите пароль администратора: ")
                    if request == admin_passwd:
                        result = csv_read(cfg)
                        for item in result:
                            print(item)
                    else:
                        print("Не верный пароль администратора!\n")
                else:
                    print("Данных нет!")
            case 4:
                break
            case _:
                print("Не верный ввод!")
