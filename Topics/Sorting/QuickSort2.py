from typing import List


def quicksort(array: List, start: int, end: int):
    if start >= end:
        return

    pivot = partition(array, start, end)

    quicksort(array, start, pivot - 1)
    quicksort(array, pivot + 1, end)


def partition(array: List, start: int, end: int):
    i = start - 1
    pivot = array[end]

    for j in range(start, end):
        if array[j] < pivot:
            i += 1
            temp = array[j]
            array[j] = array[i]
            array[i] = temp

    i += 1
    temp = array[i]
    array[i] = array[end]
    array[end] = temp

    return i


def driver():
    array = [8, 2, 4, 7, 1, 3, 9, 6, 5]
    quicksort(array, 0, len(array) - 1)
    print(array)
