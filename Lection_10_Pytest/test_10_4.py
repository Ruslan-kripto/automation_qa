# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest


@pytest.mark.usefixtures('time_start_end')
class TestClass:
    def __int__(self, a, b):
        self.a = a
        self.b = b

    def plus(self, a, b):
        return a + b

    def test_01(self, time_run_test):
        assert self.plus(2, 2) == 4

    def test_02(self, time_run_test):
        assert self.plus(-4, 2) == -2

    def test_03(self):
        assert self.plus(6, 0) == 6
