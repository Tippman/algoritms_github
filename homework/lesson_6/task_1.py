"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
from memory_profiler import profile
from time import time
from random import randint

"""поиск суммы элементов ряда чисел 1 -0.5 0.25 и т.д."""
elems_count = 900


@profile
def recursion(el_cnt):
    def task4(num, result=1):
        if num == 0:
            return 0
        else:
            return num + task4(num - 1, result / -2)
    print(task4(el_cnt))


"""наполнение словаря большим количеством элементов"""


@profile
def time_to_update_dict(dict_1={}):
    start_time = time()
    for i in range(30000):
        dict_1[f'key_{i}'] = randint(1, 1000)
    end_time = time()
    print(end_time - start_time)


recursion(elems_count)
time_to_update_dict()

"""
Результаты:

Рекурсия.
Line #    Mem usage    Increment   Line Contents
================================================
    21     10.6 MiB     10.6 MiB   @profile
    22                             def recursion(el_cnt):
    23     12.0 MiB      0.0 MiB       def task4(num, result = 1):
    24     12.0 MiB      0.0 MiB           if num == 0:
    25     12.0 MiB      0.0 MiB               return 0
    26                                     else:
    27     12.0 MiB      0.0 MiB               return num + task4(num - 1, result / -2)
    28     12.0 MiB      0.0 MiB       print(task4(el_cnt))
Рекурсия создает стек, поэтому память используется интенсивнее.


Наполнение словаря элементами.
Line #    Mem usage    Increment   Line Contents
================================================
    30     12.0 MiB     12.0 MiB   @profile
    31                             def time_to_update_dict(dict_1={}):
    32     12.0 MiB      0.0 MiB       start_time = time()
    33     15.8 MiB      0.0 MiB       for i in range(30000):
    34     15.8 MiB      1.3 MiB           dict_1[f'key_{i}'] = randint(1, 1000)
    35     15.8 MiB      0.0 MiB       end_time = time()
    36     15.8 MiB      0.0 MiB       print(end_time - start_time)
Заполение словаря большим количеством элементов.

ОС - MacOS Catalina, x64, python 3.8.2
"""
