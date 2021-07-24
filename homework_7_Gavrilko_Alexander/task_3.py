"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

Важно: стройте массив именно по формуле 2m+1
Потому что параметр m вам пригодится при поиске медианы, когда массив будет отсортирован.
Этот парамет m вам нужно запрашивать у пользователя.

[5, 3, 4, 3, 3, 3, 3]

[3, 3, 3, 3, 3, 4, 5]

my_lst
new_lts

arr[m]


from statistics import median

[3, 4, 3, 3, 5, 3, 3]

left = []
right = []

left == right and

for i in
    for
    left == right
    left.clear()
    right.clear()


"""
import random
from statistics import median

value_m = int(input('Введите m для массива размером 2m+1: '))

array = [random.randint(0, 50) for _ in range(2 * value_m +1)]
print(f'Массив: {array}')

''' Вариант 1 (цикл) '''
array_copy = array[:]
for i in range(len(array_copy)//2):
    array_copy.remove(max(array_copy))
print(f'\nМедиана: {max(array_copy)}\nПроверка: {max(array_copy) == median(array)}')

''' Вариант 2 (Шелла) '''


def shella(array):
    middle_element = len(array) // 2

    while middle_element:
        for i, j in enumerate(array):
            while i >= middle_element and array[i - middle_element] > j:
                array[i]  = array[i - middle_element]
                i -= middle_element
            array[i] = j
        middle_element = 1 if middle_element == 2 else int(middle_element * 5.0 // 11)
    return array[len(array) // 2]

print(f'\nМедиана по сортировке Шелла: {shella(array[:])}\nПроверка: {shella(array[:]) == median(array[:])}')


def gnome(array):
    i = 0

    while i < len(array) - 1:
        if array[i] <= array[i+1]:
            i += 1
        else:
            array[i], array[i+1] = array[i+1], array[i]
            j = i - 1
            while array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                if j > 0:
                    j -= 1
                else:
                    break
            i += 1
    return array[len(array) // 2]

print(f'\nМедиана по сортировке Гномья: {gnome(array[:])}\nПроверка: {gnome(array[:]) == median(array[:])}')