
def binary_search(array, left, right, target):
    if left > right:
        return -1

    middle = (left + right) // 2

    if array[middle] == target:
        return middle

    if array[middle] > target:
        return binary_search(array, left, middle - 1, target)
    else:
        return binary_search(array, middle + 1, right, target)


def test():
    array = [-1, 0, 1, 2, 3, 4, 7, 9, 10, 20]
    target = 10

    result = binary_search(array, 0, len(array) - 1, target)
    print(result)
    