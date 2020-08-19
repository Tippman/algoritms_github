"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import operator
from random import random


def merge_sort(arr, compare=operator.lt):
    """функция разделяет массив пополам, пока его длина не достигнет 1 элемента"""
    if len(arr) < 2:
        return arr[:]
    else:
        middle = int(len(arr) / 2)
        left = merge_sort(arr[:middle], compare)
        right = merge_sort(arr[middle:], compare)
        # возвращаем функцию слияния как только сформируется стек
        return merge(left, right, compare)


def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


len_array = int(input('Введите число элементов: '))
array = [random() * 50 for _ in range(len_array)]
print('Исходный массив', array)
print('Отсортированный массив', merge_sort(array))
