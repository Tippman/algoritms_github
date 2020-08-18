"""
Задание 2.
Предложить варианты оптимизации и доказать (наглядно, кодом) их эффективность
"""
from memory_profiler import profile
from random import randint, random
from numpy import array


@profile
def func1():
    l = [random()**2 for _ in range(100000)]
    del l
    return None



@profile
def func2():
    k = array([random()**2 for _ in range(100000)])
    del k
    return None

func1()
print(func2())

"""
Функция 1. В памяти под генератор списка выделено 6.3 миб, при этом после удаления ссылки 
память освободилась только на 0.6 миб

Line #    Mem usage    Increment   Line Contents
================================================
    10     22.4 MiB     22.4 MiB   @profile
    11                             def func1():
    12     28.7 MiB      0.7 MiB       l = [random()**2 for _ in range(100000)]
    13     28.1 MiB      0.0 MiB       del l
    14     28.1 MiB      0.0 MiB       return None


Функция 2. Использовался модуль numpy.array в результате под массив было выделено всего 0.9 миб, 
при удалении высвободилось 0.1 миб

Line #    Mem usage    Increment   Line Contents
================================================
    18     27.9 MiB     27.9 MiB   @profile
    19                             def func2():
    20     28.8 MiB      0.8 MiB       k = array([random()**2 for _ in range(100000)])
    21     28.7 MiB      0.0 MiB       del k
    22     28.7 MiB      0.0 MiB       return None
"""