"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою!!! версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.
"""

from collections import Counter, deque

def string_code(string):
    string_counter = Counter(string)

    string_deque = deque(sorted(string_counter.items(), key=lambda x: x[1]))
    # print(string_deque)
    if len(string_deque) != 1:
        while len(string_deque) > 1:
            size = string_deque[0][1] + string_deque[1][1]
            # print(size)
            weight = {
                0: string_deque.popleft()[0],
                1: string_deque.popleft()[0]
            }
            # print(weight)
            for  i, j in enumerate(string_deque):
                if size > j[1]:
                    # print(f'Size {size}|{j[1]}')
                    # print(f'CONTINUE i - {i}, j - {j}, j[1] - {j[1]}\n')
                    continue
                else:
                    string_deque.insert(i, (weight, size))
                    # print(f'Size {size}|{j[1]}')
                    # print(f'BREAK i - {i}, j - {j}, j[1] - {j[1]}\n')
                    break
            else:
                string_deque.append((weight, size))
    else:
        size = string_deque[0][1]
        # print(size)
        weight = {0: string_deque.popleft()[0], 1: None}
        # print(weight)
        string_deque.append((weight, size))


    return string_deque[0][0]

table = dict()

def code(s, path=''):

    if not isinstance(s, dict):
        table[s] = path

    else:
        code(s[0], path=f'{path}0')
        code(s[1], path=f'{path}1')

code(string_code("Hello!"))
print(table)