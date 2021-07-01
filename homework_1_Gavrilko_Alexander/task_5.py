"""
Задание 5.
Задание на закрепление навыков работы со стеком

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях

Подсказка:
Отдельне стопки можно реализовать через:
1) созд-е экземпляров стека (если стопка - класс)
или
2) lst = [[], [], [], [],....]

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""




class StackClass:
    def __init__(self):
        self.elems = []
        self.sum_count = 0

    def update(self):
        self.elems = []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        self.elems.append(el)


    def stack_size(self):
        return len(self.elems)



def stack_to(size, size_el):

    stacks = StackClass()
    list_stack = list()
    while True:
        for _ in range(size_el):
            stacks.push_in('T')
        if size - (stacks.sum_count + size_el) < size_el:
            list_stack.append(stacks.elems)
            stacks.update()
            for _ in range(size - (stacks.sum_count + size_el)):
                stacks.push_in('T')
            list_stack.append(stacks.elems)
            break
        else:
            list_stack.append(stacks.elems)
            stacks.update()
            stacks.sum_count += size_el


    print(list_stack)

stack_to(17, 5)
stack_to(12, 10)
stack_to(20, 8)










