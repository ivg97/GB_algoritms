"""
2. Написать программу сложения и умножения двух шестнадцатиричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)

__mul__
__add__

Пример:
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’]
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

1. вариант
defaultdict(list)
int(, 16)
reduce

2. вариант
class HexNumber:
    __add__
    __mul__

hx = HexNumber
hx + hx
hex()
"""

from collections import deque

# class HexNumber:
#     def __init__(self, x):
#         self.x = x
#
#
#     def __add__(self, other):
#         self.sum = self.x + other.x
#         return self.sum
#
#     def __mul__(self, other):
#         return self.x * self.x
#
# first_value = input('Введите первое число: ')
# second_value = input('Ввдеите второе число: ')
#
# first_value = hex(int(first_value, base=16))
# second_value = hex(int(second_value, base=16))
#
# hex_num_1 = HexNumber(first_value)
# hex_num_2 = HexNumber(second_value)

NUM = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

def sum_hex(x, y):
    result = deque()
    transfer = 0
    if len(y) > len(x):
        x, y = deque(y), deque(x)
    else:
        x, y = deque(x), deque(y)
    while x:
        if y:
            res = NUM[x.pop()] + NUM[y.pop()] + transfer
        else:
            res = NUM[x.pop()] + transfer
        transfer = 0
        if res < 16:
            result.appendleft(NUM[res])
        else:
            result.appendleft(NUM[res - 16])
            transfer = 1
    if transfer:
        result.appendleft('1')
    return list(result)


def mult_hex(x, y):
    result = deque()
    spam = deque([deque() for _ in range(len(y))])
    x, y = x, deque(y)
    for i in range(len(y)):
        m = NUM[y.pop()]
        for j in range(len(x) - 1, -1, -1):
            spam[i].appendleft(m * NUM[x[j]])
        for _ in range(i):
            spam[i].append(0)
    transfer = 0
    for _ in range(len(spam[-1])):
        res = transfer
        for i in range(len(spam)):
            if spam[i]:
                res += spam[i].pop()
        if res < 16:
            result.appendleft(NUM[res])
        else:
            result.appendleft(NUM[res % 16])
            transfer = res // 16
    if transfer:
            result.appendleft(NUM[transfer])

    return list(result)


first_value = input('Введите первое число: ')
second_value = input('Ввдеите второе число: ')


print(f"Сумма - {sum_hex(first_value, second_value)}")
print(f"Произведение - {mult_hex(first_value, second_value)}")