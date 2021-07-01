"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества
Можно воспользоваться ф-цией hash() (см. материалы к уроку)

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""


string = input('Введите строку: ')
s_set = set()
for i in range(len(string)):
    for j in range(len(string) - 1 if i == 0 else len(string), i, -1):
        s_set.add(hash(string[i:j]))

print(f'{string} - {len(s_set)} уникальных подстрок')