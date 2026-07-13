def find_boundary(arr: list[bool]) -> int:
    left = 0
    right = len(arr) - 1
    boundary = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid]:
            boundary = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary

def driver():
    arr = [False, False, True, True, True]
    boundary = find_boundary(arr)
    print(boundary)
