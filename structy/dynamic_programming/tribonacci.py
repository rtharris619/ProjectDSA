def tribonacci(n):
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)

def tribonacci_memo(n, memo):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1
    memo[n] = tribonacci_memo(n - 1, memo) + tribonacci_memo(n - 2, memo) + tribonacci_memo(n - 3, memo)
    return memo[n]

def driver():
    res = tribonacci_memo(37, {}) # -> 13
    print(res)