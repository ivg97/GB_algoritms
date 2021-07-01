"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш.

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей.

Самый просто вариант хранения хешей - просто в оперативной памяти (в переменных).

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Обязательно усложните задачу! Добавьте сохранение хеша в файле и получение его из файла.
А если вы знаете как через Python работать с БД, привяжите к заданию БД и сохраняйте хеши там.
"""

import sqlite3
import hashlib
from uuid import uuid4

connect = sqlite3.connect('arch_p.db')
cursor = connect.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
pass TEXT);
''')
connect.commit()



def registratios(password):
    salt = uuid4().hex
    password = hashlib.sha256(salt.encode() + str(password).encode()).hexdigest()
    password = [(password,)]
    cursor.executemany('''
    INSERT INTO users
    VALUES (?);
    ''', password)
    connect.commit()

    cursor.execute('SELECT pass FROM users;')
    pass_in_db = cursor.fetchone()
    print(f'В базе данных хранится строка: {pass_in_db}')
    password_2 = input('Введите еще раз пароль для проверки: ')
    password_2 = (hashlib.sha256(salt.encode() + password_2.encode()).hexdigest(),)
    if pass_in_db == password_2:
        print('Вы ввели правильный пароль!')
    else:
        print('Вы ошиблись!')

    cursor.executemany('DELETE FROM users WHERE pass= (?);', password)
    connect.commit()


password = input('Введите пароль: ')
registratios(password)
