import math

def summing_squares(n):
    return _summing_squares(n, {})

def _summing_squares(n, memo):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0

    min_squares = math.inf
    for i in range(1, math.floor(math.sqrt(n)) + 1):
        square = i * i
        num_squares = 1 + _summing_squares(n - square, memo)
        min_squares = min(num_squares, min_squares)
    memo[n] = min_squares
    return memo[n]

def driver():
    # Given 12:
    # summing_squares(12) -> 3
    # The minimum squares required for 12 is three, by doing 4 + 4 + 4.
    # Another way to make 12 is 9 + 1 + 1 + 1, but that requires four perfect squares.
    res = summing_squares(12) # -> 3
    print(res)
    res = summing_squares(10) # -> 2
    print(res)
    res = summing_squares(87) # -> 4
    print(res)