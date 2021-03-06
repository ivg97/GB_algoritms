"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается

И прошу вас обратить внимание, что то, что часто ошибочно называют генераторами списков,
на самом деле к генераторам отношения не имеет. Это называется "списковое включение" - list comprehension.
"""

from timeit import timeit
nums = [i for i in range(1000)]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

print(f"func_1 - {timeit('func_1', 'from __main__ import func_1')}")


def my_func_1(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr

print(f"my_func_1 - {timeit('my_func_1', 'from __main__ import my_func_1')}")



def enumerate_func_1(nums):
    new_arr = [i for i, j in enumerate(nums) if j % 2 == 0]
    return new_arr

print(f"enumarate_func_1 - {timeit('enumerate_func_1', 'from __main__ import enumerate_func_1')}")



'''
В предоставленной задаче был использован цикл для перебора всех значений и нахождения 
индексов четного элемента. 
Для упрощения решения я сперва попробовал реализовать LC, для наполнения списка, особой
экономии времени не было заметно. Подумав, использовал функцию enumerate. Как вы 
говорили все стандартные функции заточены на минимальное время. После замера, тот же результат.
Особой экономии времени не встретил, лишь доли секунд показали незначительное умеьшение времени.
'''