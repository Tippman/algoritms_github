"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""
from timeit import timeit

first_arr = [1, 23, 53, 8, 7, 7, 8, 8, 6, 4, 8, 4, 654]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums, new_list=[], i=0):
    if len(nums) == 0:
        return new_list
    else:
        if nums[0] % 2 == 0:
            new_list.append(i)
        nums.pop(0)
        return func_2(nums, new_list, i + 1)


print('timer #1, base function')
print(timeit("func_1(first_arr)", "from __main__ import func_1, first_arr"))
print(func_1(first_arr))
print()
print('timer #2, recursion function')
print(timeit("func_2(first_arr)", "from __main__ import func_2, first_arr"))
print(func_2(first_arr))
print()
