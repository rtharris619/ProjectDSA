from typing import List


def bubble_sort(array: List[int]):

    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def driver():
    array = [8, 2, 4, 7, 1, 3, 9, 6, 5]
    bubble_sort(array)
    print(array)
