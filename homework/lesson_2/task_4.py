"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
elems_count = int(input('введите число: '))
start_number = 1
result = 0


def task4(counter, start_number, result):
    if counter == 0:
        return result
    else:
        return task4(counter - 1, start_number / -2, result + start_number)


print(task4(elems_count, start_number, result))
