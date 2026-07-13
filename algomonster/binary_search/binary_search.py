
# O(log(n))
def binary_search(arr: list[int], target: int) -> int:
    n = len(arr)
    left = 0
    right = n - 1

    while left <= right:
        mid = (right + left) // 2
        val = arr[mid]
        if val == target:
            return mid
        elif val < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def driver():
    result = binary_search([1, 3, 5, 7, 8], 5)
    print(result)

    result = binary_search([2, 8, 89, 120, 1000], 120)
    print(result)