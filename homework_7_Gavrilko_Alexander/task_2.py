"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти).

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

import random, timeit



arr_n = int(input('Введите число элементов: '))
array = [random.uniform(0, 50) for _ in range(arr_n)]
print(f'Исходный массив: \n {array}')

def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list

def sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left_list = sort(nums[:mid])
    right_list = sort(nums[mid:])
    return merge(left_list, right_list)

print(f'Отсортированный массив: \n {sort(array)}')

print('Время: ',
    timeit.timeit(
        'sort(array[:])',
        globals=globals(),
        number=1000
    )
)


"""
arr_n = 10 элементов - Время:  0.031065992999856462
arr_n = 100 элементов - Время:  0.2598850039998979
arr_n = 1000 элементов - Время:  3.088119215000006
"""