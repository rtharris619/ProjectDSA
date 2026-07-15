def first_not_smaller(arr: list[int], target: int) -> int:
    boundary = -1
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            boundary = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary

def driver():
    arr = [1, 3, 3, 5, 8, 8, 10]
    target = 2
    index = first_not_smaller(arr, target)
    print(index)

    arr = [2, 3, 5, 7, 11, 13, 17, 19]
    target = 6
    index = first_not_smaller(arr, target)
    print(index)
