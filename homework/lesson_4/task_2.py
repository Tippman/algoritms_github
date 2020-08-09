"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""
from timeit import timeit


def memorize(func):
    """создаем декоратор, время выполнения функции с рекурсией при этом значительно снижается"""
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r
    return g


@memorize
def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


def recursive_reverse_2(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


def task_2(number):
    return str(number)[::-1]


print('Замер №1. Рекурсия без мемоизации')
print(
    timeit(
        "recursive_reverse_2(8571689)",
        "from __main__ import recursive_reverse_2"))
print()
print('Замер №2. Рекурсия с мемоизацией')
print(
    timeit(
        "recursive_reverse(8571689)",
        "from __main__ import recursive_reverse"))
print()
print('Замер №3. Обратный срез')
print(timeit("task_2(8571689)", "from __main__ import task_2"))
