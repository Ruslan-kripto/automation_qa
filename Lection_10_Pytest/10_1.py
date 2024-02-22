# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random


def generate_random_name(start=True, end=None):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if end is False:
        start, end = False, start
    while start is not False:
        name = ''.join(random.choices(alphabet, k=random.randrange(1, 16)))
        surname = ''.join(random.choices(alphabet, k=random.randrange(1, 16)))
        random_name = f'{name} {surname}'
        yield random_name


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
