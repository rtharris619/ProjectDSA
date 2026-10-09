def counting_change(amount, coins):
    return _counting_change(amount, coins, 0, {})

def _counting_change(amount, coins, i, memo):
    key = (amount, i)
    if key in memo:
        return memo[key]
    if amount == 0:
        return 1
    if i == len(coins):
        return 0

    coin = coins[i]
    ways = 0
    for qty in range(0, (amount // coin) + 1):
        remainder = amount - (qty * coin)
        ways += _counting_change(remainder, coins, i + 1, memo)
    memo[key] = ways
    return memo[key]

def driver():
    # For example,
    # counting_change(4, [1,2,3]) -> 4

    # There are four different ways to make an amount of 4:

    # 1. 1 + 1 + 1 + 1
    # 2. 1 + 1 + 2
    # 3. 1 + 3
    # 4. 2 + 2
    res = counting_change(4, [1, 2, 3]) # -> 4
    print(res)
    