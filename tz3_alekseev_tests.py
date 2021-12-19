import tz3_alekssev
import functools
import statistics


names_w_arrays = {
    "check.txt": tz3_alekssev.get_array("check.txt"),
    "check2.txt": tz3_alekssev.get_array("check2.txt"),
    "check3.txt": tz3_alekssev.get_array("check3.txt"),
    "check4.txt": tz3_alekssev.get_array("check4.txt"),
    "check5.txt": tz3_alekssev.get_array("check5.txt"),
    "check6.txt": tz3_alekssev.get_array("check6.txt"),
    "check7.txt": tz3_alekssev.get_array("check7.txt"),
}

def test_minimum_search():
    """Протестриуем функцию нахождения минимума для каждого списка"""
    for array in names_w_arrays.values():
        assert min(array) == tz3_alekssev.minimum_search(array)

def test_maximum_search():
    """Протестриуем функцию нахождения максимума для каждого списка"""
    for array in names_w_arrays.values():
        assert max(array) == tz3_alekssev.maximum_search(array)

def test_sum_get():
    """Протестриуем функцию нахождения суммы для каждого списка"""
    for array in names_w_arrays.values():
        assert sum(array) == tz3_alekssev.sum_get(array)

def test_prod_get():
    """Протестриуем функцию нахождения произведения для каждого списка"""
    for array in names_w_arrays.values():
        assert functools.reduce((lambda x, y: x * y), array) == tz3_alekssev.prod_get(array)

def test_search_median():
    """Протестируем функцию нахождения медианных значений"""
    for array in names_w_arrays.values():
        if array:
            assert statistics.median(array) == tz3_alekssev.search_median(array)
            continue
        assert None is tz3_alekssev.search_median(array)

def test_check_called_time():
    """Протестируем, как минимальное время исполнения растет с ростом размера файла"""
    for name, array in names_w_arrays.items():
        print(f"Для файла {name} минимальное время исполнения за 30 попыток составило"
              f"{tz3_alekssev.check_called(name, 30)}.")
