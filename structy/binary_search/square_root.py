def square_root(n):
    left = 0
    right = n
    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid * mid
        if mid_squared == n:
            return mid
        elif mid_squared < n:
            left = mid + 1
        else:
            right = mid - 1
        
    return right

def driver():
    res = square_root(16) # -> 4
    print(res)
    res = square_root(81) # -> 9
    print(res)
    res = square_root(204) # ->14
    print(res)