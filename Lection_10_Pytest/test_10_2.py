# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test1():
    assert all_division(6, 3) == 2.0


@pytest.mark.smoke
def test2():
    with pytest.raises(ZeroDivisionError):
        all_division(2, 0)


def test3():
    assert all_division(7, 2) == 3.5


def test_check4():
    assert all_division(4, 4) == 1


def test_check5():
    assert all_division(2, 5) == 0.4


# pytest -v
# pytest -m smoke -v
# pytest -k test_check -v
