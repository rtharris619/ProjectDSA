def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def driver():
    res = factorial(18)
    print(res)
