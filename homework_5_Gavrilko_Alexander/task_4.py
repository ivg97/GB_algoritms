"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from timeit import timeit
from collections import OrderedDict

def ordered_dictionary():
    ord_dct = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    return ord_dct

def dictionary():
    dct = dict([('a', 1), ('b', 2), ('c', 3)])
    return dct

print(f"Ordered Dictionary - {timeit('ordered_dictionary()', 'from __main__ import ordered_dictionary')}")
print(f"Dictionary - {timeit('dictionary()', 'from __main__ import dictionary')}\n")


ord_dct = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
dct = dict([('a', 1), ('b', 2), ('c', 3)])


def ord_dict_append():
    ord_dct['d'] = 4
    ord_dct['e'] = 5
    return ord_dct

def dict_append():
    dct['d'] = 4
    dct['e'] = 4
    return dct

print(f"Ordered Dictionary  append - {timeit('ord_dict_append()', 'from __main__ import ord_dict_append')}")
print(f"Dictionary  append - {timeit('dict_append()', 'from __main__ import dict_append')}\n")

ord_dct = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
dct = dict([('a', 1), ('b', 2), ('c', 3)])

def ord_dict_get():
    return ord_dct['a']


def dict_get():
    return dct['a']

print(f"Ordered Dictionary  get - {timeit('ord_dict_get()', 'from __main__ import ord_dict_get')}")
print(f"Dictionary  append - {timeit('dict_get()', 'from __main__ import dict_get')}\n")




'''
Судя по полученным результатам, то Ordered Dictionary не торопится выполнять порученные 
ему дествия. В каждом из замерах Ordered Dictionary  уступает по времени выполнения.
Видно в он был написал для использования в более ранних версиях языка, для сохранения 
порядка элементов. И с настоящее время им мало кто пользуется. Нет смысла
'''