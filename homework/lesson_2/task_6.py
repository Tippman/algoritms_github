"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

from random import randint

quest_number = randint(0, 100)
try_counter = 1


def task6(quest_number, try_counter):
    if try_counter == 11:
        print(f'Вы проиграли. Загаданное число: {quest_number}')
    else:
        print(f'Попытка № {try_counter}')
        user_answear = int(input('Введите число от 1 до 100 '))
        if user_answear == quest_number:
            return print(f'Вы отгадали загаданное число {quest_number}')
        elif user_answear > quest_number:
            print(
                f'Загаданное число меньше. Попробуйте снова. Осталось {10 - try_counter} попыток')
        else:
            print(
                f'Загаданное число больше. Попробуйте снова. Осталось {10 - try_counter} попыток')
        return task6(quest_number, try_counter + 1)


task6(quest_number, try_counter)
