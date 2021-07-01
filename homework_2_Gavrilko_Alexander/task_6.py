"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Подсказка:
Базовый случай здесь - угадали число или закончились попытки

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

import random

def guess_number(count_attermpt = 10):
    random_value = random.randint(0, 100)
    def guess(random_value, count_attermpt):
        if count_attermpt == 0:
            return f'Осталось {count_attermpt} попыток'
        user_value = int(input('Введите число от 0 до 100: '))
        if user_value == random_value:
            return 'Вы победили'
        elif user_value > random_value:
            count_attermpt -= 1
            print(f'Ваше число больше загаданного, осталось попыток: {count_attermpt} ')
            return guess(random_value, count_attermpt)
        elif user_value < random_value:
            count_attermpt -= 1
            print(f'Ваше число меньше загадонного, осталось попыток: {count_attermpt} ')
            return guess(random_value, count_attermpt)
    return guess(random_value, count_attermpt)

print(guess_number())




