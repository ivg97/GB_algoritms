"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать сложность каждого из двух алгоритмов. Для лучшего закрепления темы
можете определить и указать сложность еще и у каждого выражения этих двух алгоритмов.

Примечание:
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Постарайтесь не использовать ф-ции min() и sort() и другие ф-ции!
Подход должен быть максимально алгоритмическим.
"""

import random
lst = list()
for i in range(100):
    lst.append(random.randint(1, 100))

print(lst)


"""
1 -------- O(n)
"""

def first_alg(lst):
    '''Search min value'''
    a = lst[0]          # O(1)
    for i in lst:       # O(n)
        if i < a:       # O(1)
            a = i       # O(1)
    return a            # O(1)

print(first_alg(lst))


"""
2 ---------- O(n^2)
"""

def second_alg(lst):
    '''Search min value'''
    a = lst[0]                  # O(1)
    for i in lst:               # O(n)
        for j in lst:           # O(n)
            if i < j:           # O(1)
                if i < a:       # O(1)
                    a = i       # O(1)
            else:               # O(1)
                if j < a:       # O(1)
                    a = j       # O(1)
    return a                    # O(1)

print(second_alg(lst))