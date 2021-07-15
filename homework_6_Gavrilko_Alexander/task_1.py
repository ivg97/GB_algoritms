"""
Задание 1.

Выполните профилирование памяти в скриптах.
Проанализируйте результат и определите программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

from memory_profiler import profile, memory_usage
from timeit import default_timer

def decor(func):
    def wrapper(*args, **kwargs):
        start_m, memory_1 = default_timer(), memory_usage()
        result = func(*args, **kwargs)
        finish_m, memory_2 = default_timer(), memory_usage()
        # print(finish[0] - start[0])
        return result, finish_m - start_m, memory_2[0] - memory_1[0]
    return wrapper



'''
Урок 3, задание 2
'''


'''
Thesaurus:
Time: 0.146116214000358
Memory: 0.296875 Mib
RESAULT: {'А': ['Анастания'], 'И': ['Иван', 'Илья', 'Иван'], 'М': ['Мария'], 'О': ['Ольга'], 'П': ['Петр']}

Реализовано 1 решение, упростить не получилось
'''
@decor
@profile
def thesaurus(*args):
    ''' return sorted dictionary and print simple dictionary '''
    name_dict = {}
    for i in args:
        if i[0] in name_dict.keys():
            name_dict[i[0]].append(i)
        else:
            name_dict[i[0]] = [i]
    # print(name_dict)

#     Сортировка по ключам
    name_list = list(name_dict.keys())
    name_list.sort()
    sort_name_dict = dict()
    for i in name_list:
        sort_name_dict[i] = name_dict[i]
    return sort_name_dict

# thesaurus("Иван", "Мария", "Петр", "Илья", "Иван", "Анастания", "Ольга")

'''
Урок 3, задание 3
'''

'''
Get_jokes:
Time: 0.11697523999828263
Memory: 0.0 Mib
RESAULT: ['дом позавчера мягкий', 'автомобиль завтра зеленый', 'лес сегодня яркий', 'огонь ночью утопичный', 'город вчера веселый']

Реализовано 1 решение, упростить не получилось, особо и не требуется
'''

from random import choice

@decor
@profile
def get_jokes(quantity, flag=True):
    ''' return n joke '''
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    if quantity > min(len(nouns), len(adverbs), len(adjectives)):
        error = f'Данное количество шуток не может быть сгенерировано'
        return error

    return_jokes = list()
    if flag:
        for i in range(0, quantity):
            joke = f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}'
            return_jokes.append(joke)
        return return_jokes

    nouns_flag = nouns.copy()
    adverbs_flag = adverbs.copy()
    adjectives_flag = adjectives.copy()
    for i in range(0, quantity):
        rand_nouns, rand_adverbs, rand_adjective = choice(nouns_flag), \
                                                   choice(adverbs_flag), \
                                                   choice(adjectives_flag)
        joke = f'{rand_nouns} {rand_adverbs} {rand_adjective}'
        nouns_flag.remove(rand_nouns)
        adverbs_flag.remove(rand_adverbs)
        adjectives_flag.remove(rand_adjective)
        return_jokes.append(joke)
    return return_jokes





'''
Урок 4, задание 2
'''

'''
Currency_rates:
Time: 0.1952638590009883
Memory: 0.47265625 Mib
RESAULT: 74.1236


Реализовано 1 решение, упростить не получилось. Пытался найти другие решения,
но становилось тольок хуже
'''

import requests

@decor
@profile
def currency_rates(currency):
    '''  '''
    response = requests.get(' http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = requests.utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    for id in content.split('<Valute ID='):
        index_currency = id.find(currency)
        if index_currency != -1:
            value_currenty = id.split('Value')[-2][1:-2:]
            return float(value_currenty.replace(',', '.'))



'''
Урок 6, задание 1
'''

'''
Log:
Time: 42.007946205001645
Memory: 3.15234375 Mib
RESAULT: Спамер - 216.46.173.126


Задача решалась с помощью списков и словарей, занимает много памяти и времени
'''

ip_list = list()
ip = {}

@decor
@profile
def log():
    with open('nginx_logs.txt', encoding='utf-8') as f:
        for line in f:
            line = line.strip().split()
            ip_list.append(line[0])

    for i in ip_list:
        ip_count = ip_list.count(i)
        ip[ip_count] = i
    max_count = max(ip.keys())
    return f'Спамер - {ip[max_count]}'



'''Вариант 2 урок 6 задание 1'''

'''
Log_2:
Time: 6.409366260999377
Memory: 3.09375 Mib
RESAULT: Спамер - 216.46.173.126

В данном решении использовал Counter. Памяти много не освобоилось, но 
значительно ускорился процесс. Результат на лицо
'''

from collections import Counter

ip_list_2 = []

@decor
@profile
def log_2():
    with open('nginx_logs.txt', encoding='utf-8') as f:
        for line in f:
            ip_list_2.append(line.strip().split()[0])

    ip_2 = Counter(ip_list_2)
    return f'Спамер - {max(ip_2, key=lambda x: ip_2[x])}'


''' Задача 4 '''

'''
Othen:
Time: 0.18308506200264674
Memory: 0.0 Mib
RESAULT: В массиве чаще всего встречается число 7. Количество повторений: 10

В задаче использовался метод рандом для наполнения списка. Во втором варианте 
решил попробовать наполнить список с помощью генератора, ускорить не получилось
'''

import random

@decor
@profile
def often():
    mas_num = [random.randint(1, 9) for _ in range(50)]

    num = 0
    count_num = 0

    for i in set(mas_num):
        count = 0

        for j in mas_num:
            if i == j:
                count += 1

        if count > count_num:
            count_num = count
            num = i

    return f'В массиве чаще всего встречается число {num}. '\
            f'Количество повторений: {count_num}'

''' Задача 4 вариант 2'''

'''
Othen_2:
Time: 0.20012895000036224
Memory: 0.0 Mib
RESAULT: В массиве чаще всего встречается число 8. Количество повторений: 11

Генератор использовал больше времени, чем метод рандом. Не разобрался почему
'''


@decor
@profile
def often_2():
    def gen_mas_num(n):
        for _ in range(n):
            yield random.randint(1, 9)


    mas_num_2 = [i for i in gen_mas_num(50)]

    num_2 = 0
    count_num_2 = 0

    for i_2 in set(mas_num_2):
        count_2 = 0

        for j in mas_num_2:
            if i_2 == j:
                count_2 += 1

        if count_2 > count_num_2:
            count_num_2 = count_2
            num_2 = i_2

    return f'В массиве чаще всего встречается число {num_2}. '\
            f'Количество повторений: {count_num_2}'



''' Задание 5 Урок 5'''


'''
No_repeat:
Time: 0.11592573300004005
Memory: 0.0 Mib
RESAULT: [23, 1, 3, 10, 4, 11]


Реализовано два варианта решения, по времени и памяти почти равны
'''

@decor
@profile
def no_repeat():
    src_1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


    def inf(i, src):
        if src.count(i) == 1:
            return 1

    result_list = [i for i in src_1 if inf(i, src_1) == 1]
    return result_list

'''Вариант 2 Задание 5 Урок 5'''

'''
No_repeat_2:
Time: 0.11680307499773335
Memory:0.0 Mib
RESAULT: [23, 1, 3, 10, 4, 11]

Реализовано два варианта решения, по времени и памяти почти равны
'''


@decor
@profile
def no_repeat_2():
    src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    result_2 = []
    src2 = []
    for i in src:
        if i not in result_2:
            result_2.append(i)
        else:
            src2.append(i)
    for i in result_2:
        if i in src:
            src.remove(i)
    for i in src:
        if i in result_2:
            result_2.remove(i)
    return result_2

'''Урок 2'''

'''
Summ_cub:
Time: 0.14098610700239078
Memory: 0.296875
RESAULT: 800

Решил задачи двумя вариантам, с особой разницы не увидел, так как использованы однотипные решения
'''

@decor
@profile
def summ_cub(n):
    summ = 0
    for i in range(n + 1):
        if i % 2 == 0:
            i = i ** 3
            summ += i
    return summ

''' Урок 2 вариант 2'''

'''
Summ_cub_2:
Time: 0.10429604299861239
Memory: 0.0
RESAULT: 800

Решил задачи двумя вариантам, с особой разницы не увидел, так как использованы однотипные решения
'''

@decor
@profile
def summ_cub_2(n):
    summ_2= 0
    n = n if n % 2 == 0 else n-1
    while n > 0:
        summ_2 += n ** 3
        n -= 2
    return summ_2




if __name__ == '__main__':
    thesaurus, m, mem = thesaurus("Иван", "Мария", "Петр", "Илья", "Иван", "Анастания", "Ольга")
    get_jokes, g_m, get_mem = get_jokes(5, False)
    currency_rates, currency_rates_m, currency_rates_mem = currency_rates('USD')
    log, log_m, log_mem = log()
    log_2, log_m_2, log_2_mem = log_2()
    often, often_m, often_mem = often()
    often_2, often_m_2, often_2_mem = often_2()
    no_repeat, no_repeat_m, no_repeat_mem = no_repeat()
    no_repeat_2, no_repeat_2_m, no_repeat_2_mem = no_repeat_2()
    summ, summ_m, summ_mem = summ_cub(8)
    summ_2, summ_m_2, summ_mem_2 = summ_cub_2(8)


    print(f'Thesaurus:\nTime: {m}\nMemory: {mem} Mib\nRESAULT: {thesaurus}\n')
    print(f'Get_jokes:\nTime: {g_m}\nMemory: {get_mem} Mib\nRESAULT: {get_jokes}\n')
    print(f'Currency_rates:\nTime: {currency_rates_m}\nMemory: {currency_rates_mem} Mib\nRESAULT: {currency_rates}\n')
    print(f'Log:\nTime: {log_m}\nMemory: {log_mem} Mib\nRESAULT: {log}\n')
    print(f'Log_2:\nTime: {log_m_2}\nMemory: {log_2_mem} Mib\nRESAULT: {log_2}\n')
    print(f'Othen:\nTime: {often_m}\nMemory: {often_mem} Mib\nRESAULT: {often}\n')
    print(f'Othen_2:\nTime: {often_m_2}\nMemory: {often_2_mem} Mib\nRESAULT: {often_2}\n')
    print(f'No_repeat:\nTime: {no_repeat_m}\nMemory: {no_repeat_mem} Mib\nRESAULT: {no_repeat}\n')
    print(f'No_repeat_2:\nTime: {no_repeat_2_m}\nMemory:{no_repeat_2_mem} Mib\nRESAULT: {no_repeat_2}\n')
    print(f'Summ_cub:\nTime: {summ_m}\nMemory: {summ_mem} Mib\nRESAULT: {summ}\n')
    print(f'Summ_cub_2:\nTime: {summ_m_2}\nMemory: {summ_mem_2} Mib\nRESAULT: {summ_2}\n')


