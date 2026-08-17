def fib(n: int, memo: list[int]) -> int:
    if memo[n] != 0:
        return memo[n]
    if n <= 1:
        return n

    res = fib(n - 1, memo) + fib(n - 2, memo)
    memo[n] = res
    return res

def driver():
    n = 8
    memo = [0] * (n + 1)
    res = fib(n, memo)
    print(res)