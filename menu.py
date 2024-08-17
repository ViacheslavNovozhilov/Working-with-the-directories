from pprint import pprint

from logic import get_content_number, recieve_content_by_chosen_number, get_config, list_content


def start():
    config = get_config()
    answer = input(f"""Если вы хотите просмотреть содержимое {config.get('point_path')}, нажмите Y
    Если нет, то нажмите N\n""")
    match answer:
        case "y":
            pprint(get_content_number(list_content(config.get('point_path'))))
            answer1 = int(input("Введите номер файла или каталога - "))
            pprint(recieve_content_by_chosen_number(answer1, config))
        case "n":
            print(f"Вы находитесь в {config.get('point_path')}")
        case _:
            print(f"Вы должны ввести y или n !")
