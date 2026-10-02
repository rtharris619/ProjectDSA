def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1

def driver():
    res = binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8], 6) # -> 6
    print(res)

    res = binary_search([0, 6, 8, 12, 16, 19, 20, 24, 28], 28) # -> 8
    print(res)
