# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smoke, а 1 набор данных скипните

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('a,b,result', [pytest.param(6, 3, 2.0, id='smoke'),
                                        pytest.param(2, 0, 0, marks=pytest.mark.skip('chinim')),
                                        (7, 2, 3.5), (4, 4, 1), (2, 5, 0.4)])
def test_division(a, b, result):
    assert all_division(a, b) == result
