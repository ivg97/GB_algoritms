"""
Задание 6.
Задание на закрепление навыков работы с очередью

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например,
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""


class Queue:
    def __init__(self):
        self.queue = []
        self.queue_for_revision = []
        self.queue_for_solved = []

    def in_queue(self, task):
        self.queue.append(task)
        return self.queue

    def in_revision(self, task):
        if task in self.queue:
            self.queue.remove(task)
            self.queue_for_revision.append(task)
            return self.queue_for_revision
        else:
            print('задача не найдена')
            return self.queue_for_revision

    def complited(self, task):
        if task in self.queue:
            self.queue.remove(task)
            self.queue_for_solved.append(task)
            return self.queue_for_solved
        elif task in self.queue_for_revision:
            self.queue_for_revision.remove(task)
            self.queue_for_solved.append(task)
            return self.queue_for_solved
        else:
            print('задача не найдена')
            return self.queue_for_solved


q = Queue()
print(q.in_queue('task1'))
print(q.in_queue('task2'))
print(q.in_revision('task1'))
print(q.complited('task2'))
print(q.complited('task'))



