def catalog_finder(url_list):
    """
    Дописать функцию, которая принимает список URL, а возвращает
    список только тех URL, в которых есть /catalog/
    """

    result_list = list()
    for i in url_list:
        if i.find('/catalog/') > 0:
            result_list.append(i)

    return result_list


def get_str_center(input_str):
    """
    Дописать функцию, которая вернет Х символов из середины строки
    (2 для четного кол-ва символов, 3 - для нечетного).
    """

    length = len(input_str)
    mid = int(length / 2)
    if length % 2 == 0:
        output_str = input_str[mid - 1:mid + 1]
    else:
        output_str = input_str[mid - 1:mid + 2]

    return output_str


def count_symbols(input_str):
    """
    Дописать функцию, которая считает сколько раз каждая из букв
    встречается в строке, разложить буквы в словарь парами
    {буква:количество упоминаний в строке}
    """

    output_dict = dict()
    for i in input_str:
        if output_dict.get(i):
            value = output_dict[i]
            output_dict.update({i: value+1})
        else:
            output_dict.update({i:1})

    return output_dict


def mix_strings(str1, str2):
    """
    Дописать функцию, которая будет принимать 2 строки и вставлять вторую
    в середину первой
    """

    length = len(str1)
    mid = int(length / 2)
    result_str = str1[:mid] + str2 + str1[mid:]

    return result_str


def even_int_generator():
    """
    Сгенерировать список из диапазона чисел от 0 до 100 и записать
    в результирующий список только четные числа.
    """

    even_int_list = list()
    for i in range(100):
        if i % 2 == 0:
            even_int_list.append(i)
    return even_int_list
