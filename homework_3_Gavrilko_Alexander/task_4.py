"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносить ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""
from uuid import uuid4
import hashlib

salt = uuid4().hex

class Cach:
    def __init__(self):
        self.url_cach = dict()

    def add_url(self, url_h, url):
        self.url_cach[url] = url_h



    def check_url(self, url_h, url):
        if self.url_cach.get(url) == url_h:
            return True
        return False
cach = Cach()

def cach_chek(url):
    url_h = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    if cach.check_url(url_h, url):
        print('Страница существует!')
    else:
        cach.add_url(url_h, url)
        print('Добавлена!')

cach_chek('https://github.com/ivg97/GB_algoritms/pull/1')
cach_chek('https://github.com/ivg97/GB_algoritms/pull/2')
cach_chek('https://github.com/ivg97/GB_algoritms/pull/1')
