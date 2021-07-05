"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Обязательно предложите еще свой вариант решения и также запрофилируйте!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!

Без аналитики задание считается не принятым
"""
from cProfile import run

import timeit

def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num, lst=[]):
    for i in str(enter_num):
        lst = [i] + lst
    lst = ''.join(lst)
    return lst

def main():
    enter_run = 12345
    r1 = revers_1(enter_run)
    r2 = revers_2(enter_run)
    r3 = revers_3(enter_run)
    r4 = revers_4(enter_run)

run('main()')


print(f"revers_1 - {timeit.timeit('revers_1(enter_num=12345)', 'from __main__ import revers_1')}")
print(f"revers_2 - {timeit.timeit('revers_2(enter_num=12345)', 'from __main__ import revers_2')}")
print(f"revers_3 - {timeit.timeit('revers_3(enter_num=12345)', 'from __main__ import revers_3')}")
print(f"revers_4 - {timeit.timeit('revers_4(enter_num=12345)', 'from __main__ import revers_4')}")


'''
Из четрырех решений задачи, после замера времени видно что решение 
revers_3 т.е. решение со срезами работает быстрее всех. По моему данное решение 
самое бытрое, так как в решении меньше всего, по сравнению с другими решениями,
вычислений и использование готовых методов языка python.
'''