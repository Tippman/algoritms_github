"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""

import hashlib

string = input('Введите строку, состоящую только из строчных латинских букв: ')

sum_substring = set()

for i in range(len(string)):
    for j in range(len(string), i, -1):
        hash_str = hashlib.sha1(string[i:j].encode()).hexdigest()
        sum_substring.add(hash_str)

print(f'итого {len(sum_substring) - 1} различных подстрок в строке {string}')
