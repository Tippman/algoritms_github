"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
from time import time
from random import randint


def time_to_update_list(list_1=[]):
    start_time = time()
    for i in range(30000):
        list_1.append(randint(1, 1000))
    end_time = time()
    print(end_time - start_time)
    print(list_1)


def time_to_update_dict(dict_1={}):
    start_time = time()
    for i in range(30000):
        dict_1[f'key_{i}'] = randint(1, 1000)
    end_time = time()
    print(end_time - start_time)
    print(dict_1)


time_to_update_dict()
time_to_update_list()
