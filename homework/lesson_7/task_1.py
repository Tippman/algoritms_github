"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""
from random import randint
from timeit import timeit

start_arr = [randint(-100, 100) for _ in range(20)]
arr_to_sort_bubble = start_arr[:]
arr_to_sort_bubble_opt = start_arr[:]


def bubble_sort(arr):
    i = 1
    while i < len(arr):
        for j in range(len(arr) - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        i += 1
    return arr


def bubble_sort_opt(arr):
    i = 1
    while i < len(arr):
        flag = False  # флаг для останоки перебора в случае отсутствия перестановок
        for j in range(len(arr) - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True
        if not flag:
            break
        i += 1
    return arr


print('Начальный массив:', start_arr)
print('Отсортированный массив:', bubble_sort(arr_to_sort_bubble))
print('Отсортированный массив ОПТ:', bubble_sort_opt(arr_to_sort_bubble_opt))
print(
    'Время выполнения обычной сортировки',
    timeit(
        'bubble_sort(arr_to_sort_bubble)',
        'from __main__ import bubble_sort, arr_to_sort_bubble',
        number=10000))
print(
    'Время выполнения ОПТ сортировки',
    timeit(
        'bubble_sort_opt(arr_to_sort_bubble_opt)',
        'from __main__ import bubble_sort_opt, arr_to_sort_bubble_opt',
        number=10000))

"""оптимизация алгоритма путем исключения перебора в случае отсутствия перестановок
элементов показывает результаты только в случае отсортированного массива,
в случае генератора тоже показывает хорошие результаты относительно обычной сортировки
"""