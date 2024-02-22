import pytest
import time
import datetime


@pytest.fixture(scope='class')
def time_start_end():
    print(f'Время начала выполнения класса: {datetime.datetime.now()}')
    yield print(f'Время окончания выполнения класса: {datetime.datetime.now()}')


@pytest.fixture()
def time_run_test():
    start = time.time()
    time.sleep(2)  # делаю задержку, иначе возвращается 0
    yield print(f'Время выполнения теста: {time.time() - start}')
