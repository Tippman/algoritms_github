"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)
    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    """Используя множество не придется пробегаться по всем числам в исходном списке.
    Чем длинне список тем оптимальнее время выполнения
    """
    array_set = set(array)
    max_count = None
    qty_max_count = 0
    for i in array_set:
        qty = array.count(i)
        if qty > qty_max_count:
            qty_max_count = qty
            max_count = i
    return f'Чаще всего встречается число {max_count}, ' \
           f'оно появилось в массиве {qty_max_count} раз(а)'

    # можно решить в одну строку, но время выполнения самое худшшее
    # return f'Чаще всего встречается число {max(array, key=array.count)}, ' \
    #        f'оно появилось в массиве {array.count(max(array, key=array.count))} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print()
print('Замер func_1')
print(timeit('func_1()', 'from __main__ import func_1'))
print()
print('Замер func_2')
print(timeit('func_2()', 'from __main__ import func_2'))
print()
print('Замер func_3')
print(timeit('func_3()', 'from __main__ import func_3'))
