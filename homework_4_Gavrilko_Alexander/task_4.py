"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой и по возможности самой лаконичной.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым!
"""
import timeit


array = [1, 3, 1, 3, 4, 5, 1, 3, 3]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'

def func_3():
    ar = {}
    for i in array:
        if i in ar:
            ar[i] += 1
        else:
            ar[i] = 1
    for i,j in ar.items():
        if j == max(ar.values()):
            return f'Чаще всего встречается число {i}, '\
                    f'оно появилось в массиве {max(ar.values())} раз(а)'



# print(func_1())
# print(func_2())
# print(func_3())


print(f"func_1 - {timeit.timeit('func_1()', 'from __main__ import func_1')}")
print(f"func_2 - {timeit.timeit('func_2()', 'from __main__ import func_2')}")
print(f"func_3 - {timeit.timeit('func_3()', 'from __main__ import func_3')}")


print(f'Третий вариант решения выполнен наподобии второго, но с использованием словаря,\n'
      f'так как сложность выполнении операций со словарем, определенно меньше чем, со списком.\n'
      f'Я замерил время на всех трех решения и вот что получилось:\n'
      f'Победителем по скорости оказался первый вариант решения,\n'
      f'на втором месте оказалося мной написанный вариант решения со словарем\n'
      f'и самым долгим из всех оказался второй вариант с чувствительным отставанием от всех.\n')