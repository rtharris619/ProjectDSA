def sum_possible(amount, numbers):
    return _sum_possible(amount, numbers, {})

def _sum_possible(amount, numbers, memo) -> bool:
    if amount in memo:
        return memo[amount]    
    if amount == 0:
        return True
    if amount < 0:
        return False
    for num in numbers:
        if _sum_possible(amount - num, numbers, memo):
            memo[amount] = True
            return memo[amount]
    memo[amount] = False
    return memo[amount]

def driver():
    res = sum_possible(8, [5, 12, 4]) # -> True, 4 + 4
    print(res)
    res = sum_possible(15, [6, 2, 10, 19]) # -> False
    print(res)