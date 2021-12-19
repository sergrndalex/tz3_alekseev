import time
import functools

def prod_get(array):
    """Найдем произведение, вернем None сли в в файле нет чисел или too high,
    если произведение слишком большое и вызывает иселючение. В ином случае вернем произведение"""
    if len(array) == 0:
        return None
    output=1
    for i in array:
        try:
            output *= i
        except (OverflowError, ValueError):
            return "too high prod"
    return output


def sum_get(array):
    """
    На вход подается список
    Вернем сумму списка или None сли список пустой
    """
    if len(array) == 0:
        return None
    return functools.reduce((lambda x, y: x + y), array)


def get_array(name):
    """
    На вход подается имя файла
    возвращает список чисел
    """
    with open(name) as f:
        output = [float(numb) for line in f.readlines() for numb in line.split()]
    return output


def minimum_search(array):
    """
    На вход подается список
    Вернем минимальное значение списка или None если список пустой
    """
    if len(array) == 0:
        return None
    minvalue = array[0]
    for i in array:
        if i < minvalue:
            minvalue = i
    return minvalue

def maximum_search(array):
    """
    На вход подается список
    Вернем максимальное значение списка или None если список пустой
    """
    if len(array) == 0:
        return None
    maxvalue = array[0]
    for i in array:
        if i > maxvalue:
            maxvalue = i
    return maxvalue

def call_all_to_test(name):
    """

    Выполним все функции для того, чтобы в дальнейшем узнать время их исполнения
    Функции передается имя файла
    Функция ничего не возвращает
    """
    file = get_array(name)
    minimum_search(file)
    maximum_search(file)
    sum_get(file)
    prod_get(file)
    search_median(file)


def check_called(name, number):
    checks = []
    if isinstance(number, int):
        if number > 0:
            start = time.time()
            call_all_to_test(name)
            finish = time.time()
            checks.append(finish-start)
        checks_sum, checks_number = sum(checks), len(checks)
        return checks_sum/checks_number
    return None

def search_median(array):
    """
    Найти медиану в списке
    В функцию передается список чисел
    Функция возвращает медианное значение списка
    Если список пустой, функция вернет None
    """
    array.sort()
    n = len(array)
    return (array[n // 2 - 1] / 2.0 + array[n // 2] / 2.0, array[n // 2])[n % 2] if n else None
