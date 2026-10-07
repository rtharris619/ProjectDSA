# O(2^n) time complexity
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)

# O(n) time complexity
def fib_memo(n, memo):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

def driver():
    n = 35
    res = fib(n) # -> 9227465
    print(res)

    res = fib_memo(n, {})
    print(res)