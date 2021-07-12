"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: 
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.

В первую очередь необходимо выполнить замеры для ф-ций appendleft, popleft, extendleft дека и для их аналогов у списков.
"""

import timeit
from collections import deque

def list_create():
    lst = list(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])
    return lst


def deque_create():
    dq = deque('1234567890')
    return dq


print(f"List create - {timeit.timeit('list_create()', 'from __main__ import list_create')}")
print(f"Deque create - {timeit.timeit('deque_create()', 'from __main__ import deque_create')}\n")

lst = list(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])
dq = deque('1234567890')

def list_append():
    lst.append('11')
    lst.append('12')
    lst.append('13')
    return lst

def dq_append():
    dq.append('11')
    dq.append('12')
    dq.append('13')
    return dq



print(f"list append - {timeit.timeit('list_append()', 'from __main__ import list_append')}")
print(f"Deque append - {timeit.timeit('dq_append()', 'from __main__ import dq_append')}\n")


lst = list(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])
dq = deque('1234567890')

def list_insert():
    lst.insert(0, '11')
    lst.insert(0, '12')
    lst.insert(0, '13')
    return lst

def dq_appendleft():
    dq.appendleft('11')
    dq.appendleft('12')
    dq.appendleft('13')
    return dq


print(f"List insert - {timeit.timeit('list_insert()', 'from __main__ import list_insert', number=10000)}")
print(f"Dq appendleft - {timeit.timeit('dq_appendleft', 'from __main__ import dq_appendleft', number=10000)}\n")

lst = list(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])
dq = deque('1234567890')

def list_pop():
    lst.pop(0)
    lst.pop(0)
    lst.pop(0)
    return lst


def dq_popleft():
    dq.popleft()
    dq.popleft()
    dq.popleft()
    return dq

print(f"List pop - {timeit.timeit('list_pop()', 'from __main__ import list_pop', number=3)}")
print(f"Dq popleft - {timeit.timeit('dq_popleft()', 'from __main__ import dq_popleft', number=3)}\n")


'''
Для многих выполенных мной функций deque выигрывает по времени у list. Но есть и противоположные результаты.
Например, добавление что в списке, что в deque работает почти на равных, лишь незначимые различия во времени.
Но при добавлении в начало, списки ведут себя куда более перспективнее по сравнению с deque. Время значительно 
различимое и невыгодное у deque
'''