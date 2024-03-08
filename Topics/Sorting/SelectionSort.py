from typing import List


def selection_sort(array: List):

    for i in range(len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

    return array


def driver():
    array = [8, 2, 4, 7, 1, 3, 9, 6, 5]
    selection_sort(array)
    print(array)
