from typing import List


def insertion_sort(array: List):

    for i in range(1, len(array)):
        temp = array[i] # 1
        j = i - 1 # 0

        while j >= 0 and temp < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp


def driver():
    array = [6, 1, 7, 4, 2, 9, 8, 5, 3]
    insertion_sort(array)
    print(array)
