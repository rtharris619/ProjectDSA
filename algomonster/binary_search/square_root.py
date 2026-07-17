def square_root(n: int) -> int:
    if n == 1:
        return 1

    boundary = -1
    arr = list(range(1, n)) # [1,2,3,4]
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        square = arr[mid] ** 2
        if square == n:
            return arr[mid]
        elif square > n:
            right = mid - 1
        else:
            boundary = arr[mid]
            left = mid + 1

    return boundary

def driver():
    n = 4
    res = square_root(n)
    print(res)