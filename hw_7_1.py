# Напишите декоратор для превращения функции print в генератор html-тегов
# Декоратор должен принимать список тегов italic, bold, underline
# Результатом работы декоратора с аргументами italic, bold должно быть преобразование из строки вида "test string" в "<i><b>test string</b></i>"

import os

def str_to_html(tags):
    def decorator(func):
        tag_base = {
            "italic": f"<i>%text%</i>",
            "bold": f"<b>%text%</b>",
            "underline": f"<u>%text%</u>",
        }
        def wrapper(text):
            for tag in tags:
                f_str = tag_base.get(tag)
                text = f_str.replace("%text%",text)
            return text
        return wrapper
    return decorator


@str_to_html(["italic", "bold"])
def get_text(text):
    return text


# Напишите функцию, которая возвращает список файлов из директории.
# Напишите декоратор для этой функции, который прочитает все файлы с
# раширением .log из найденных

def log_reading(func):
    def wrapper(*args):
        files = func(path)
        for file in files:
            if file.endswith(".log"):
                with open(f"{path}/{file}", "r") as r_file:
                    print(r_file.read())
    return wrapper


@log_reading
def get_files(path):
    file_list = os.listdir(path)
    return file_list


path = "d:/"
get_files(path)