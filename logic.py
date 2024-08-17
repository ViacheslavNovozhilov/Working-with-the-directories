import os


def get_config():
    path_name = r'/'
    return {
        'path_name': path_name,
        'point_path': os.path.join(path_name)
    }


def list_content(path: str):
    return sorted(os.listdir(path))


def get_content_number(lst_content):
    content_dict = {}
    for i in range(len(lst_content)):
        content_dict[i] = lst_content[i]
    return content_dict


def is_file_check(point) -> bool:
    if os.path.isfile(point):
        return True
    return False


def is_dir_check(point):
    if os.path.isdir(point):
        return True
    return False


def recieve_content_by_chosen_number(num, config: dict):
    lst_res = list_content(config.get('point_path'))
    dict_file_dir = get_content_number(lst_res)

    file_obj = dict_file_dir[num]
    new_start_point = os.path.join(config.get('point_path'), file_obj)
    if is_file_check(new_start_point):
        with open(new_start_point, "r", encoding="utf-8") as file:
            return [line.strip() for line in file]
    elif is_dir_check(new_start_point):
        res = list_content(new_start_point)
        return get_content_number(res)
    else:
        return
