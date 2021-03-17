"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import hashlib
from uuid import uuid4

salt = uuid4().hex

"""возьмем пару адресов в виде хеша"""
url_1 = 'https://geekbrains.ru/'
url_2 = 'https://yandex.ru/'

url_hash_table = {
    1: hashlib.sha256(salt.encode() + url_1.encode()).hexdigest() + ':' + salt,
    2: hashlib.sha256(salt.encode() + url_2.encode()).hexdigest() + ':' + salt
}

"""Цикл принимает ввод адреса, хэширует его и проверяет наличие в талице"""
while True:
    input_url = input('введите адрес веб страницы или 0 для выхода: ')
    if input_url == '0':
        break
    input_url_hash = hashlib.sha256(salt.encode() + input_url.encode()).hexdigest() + ':' + salt
    if input_url_hash not in url_hash_table.values():
        url_hash_table.update({len(url_hash_table) + 1: input_url_hash})
        print('таблица кэш адресов обновлена, добавлен новый хэш')
        continue
    else:
        print('адрес уже содержится в таблице')
        continue

print(f'\nитоговая талица:')
for k, v in url_hash_table.items():
    print(k, v)
