from math import inf

def min_change(amount, coins):
    res = _min_change(amount, coins, {})
    return res if res != inf else -1

def _min_change(amount, coins, memo):
    if amount in memo:
        return memo[amount]
    if amount == 0:
        return 0
    if amount < 0:
        return inf
    
    min_coins = inf
    for coin in coins:
        min_coins = min(min_coins, _min_change(amount - coin, coins, memo) + 1)

    memo[amount] = min_coins
    return min_coins

def driver():
    res = min_change(8, [1, 5, 4, 12]) # -> 2, because 4+4 is the minimum coins possible
    print(res)
    res = min_change(271, [10, 8, 265, 24]) # -> -1
    print(res)