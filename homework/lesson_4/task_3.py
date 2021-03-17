"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import cProfile
from timeit import timeit


def revers(enter_num, revers_num=0):
    """Самая долгая функция т.к. рекурсия"""
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    """более быстрая функция т.к. используется обычный цикл"""
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    """самая быстрая функиця т.к. используется простой срез"""
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def main():
    num = 7899465132
    revers(num)
    revers_2(num)
    revers_3(num)


cProfile.run('main()')

print('замер revers')
print(timeit('revers(7899465132)', 'from __main__ import revers'))
print()
print('замер revers_2')
print(timeit('revers_2(7899465132)', 'from __main__ import revers_2'))
print()
print('замер revers_3')
print(timeit('revers_3(7899465132)', 'from __main__ import revers_3'))
