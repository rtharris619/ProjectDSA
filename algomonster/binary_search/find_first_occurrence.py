def find_first_occurrence(arr: list[int], target: int) -> int:
    boundary = -1
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            boundary = mid
            right = mid - 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return boundary

def driver():
    arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
    target = 3
    index = find_first_occurrence(arr, target)
    print(index)

    arr = [2, 3, 5, 7, 11, 13, 17, 19]
    target = 6
    index = find_first_occurrence(arr, target)
    print(index)
