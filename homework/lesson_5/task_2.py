"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""
from collections import defaultdict


def summary_16(first_num, second_num):
    res = f'{hex(int(first_num,16)+int(second_num, 16))[2:]}'
    print(f'Сумма чисел: {list(res.upper())}')


def multip_16(frst_n, sec_n):
    res = f'{hex(int(frst_n,16)*int(sec_n, 16))[2:]}'
    print(f'Произведение чисел: {list(res.upper())}')


def main():
    f = input('введите первое число в шестнадцатиричном формате: ')
    s = input('введите второе число в шестнадцатиричном формате: ')
    d = defaultdict(list)
    for i in f:
        d[f].append(i.upper())
    for j in s:
        d[s].append(j.upper())
    print(f'Введены числа:\n{d[f]} и {d[s]}')
    d['Сумма'].append(summary_16(f, s))
    d['Произведение'].append(multip_16(f, s))


main()
