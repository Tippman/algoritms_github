"""
Задание 3.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""

company_data = {
    'Walmart': 524000,
    'State Grid': 387000,
    'Sinopec Group': 369000,
    'China National Petroleum': 364100,
    'Saudi Aramco': 329800,
    'Royal Dutch Shell': 311600,
    'Toyota': 280500,
    'Bp': 278400
}

# Первый вариант. Сложность O(N log N) т.к. присутствует сортировка
print('\n', '#' * 10, 'Вариант 1', '#' * 10)

def get_top3_var_1():
    return sorted(list(company_data.items()), reverse=True)[:3]

print(get_top3_var_1())


# Второй вариант. Сложность O(N^2)
print('\n', '#' * 10, 'Вариант 2', '#' * 10)

def get_top3_var_2(random_list):
    for i in range(len(random_list)):
        lowest_value_index = i
        for j in range(i + 1, len(random_list)):
            if random_list[j][1] > random_list[lowest_value_index][1]:
                lowest_value_index = j
        random_list[i], random_list[lowest_value_index] = random_list[lowest_value_index], random_list[i]
    return random_list[0:3]

list_from_dictionary = list(company_data.items())
for i in get_top3_var_2(list_from_dictionary):
    print(i[0], ':', i[1])


"""Лучший первый вариант, т.к. самая маленькая сложность """
