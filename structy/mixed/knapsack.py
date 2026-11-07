# Write a function knapsack that takes in a list of item values, a list of item weights, and a weight limit.
# The i-th item has a value of values[i] and a weight of weights[i].

# Your job is to pick items to pack into your knapsack so that its total weight does not exceed the limit
# and the value of the items is maximized. You may either take an item once or not at all.
# You cannot take the same item multiple times. Return the maximum total value of items you can pack into the knapsack.


from math import inf


def knapsack(values, weights, weight_limit):
    return _knapsack(values, weights, weight_limit, 0, {})


def _knapsack(values: list[int], weights: list[int], weight_limit: int, i: int, cache: dict):
    key = (weight_limit, i)
    if key in cache:
        return cache[key]
    if weight_limit < 0:
        return -inf
    if i == len(values):
        return 0
    
    dont_take = _knapsack(values, weights, weight_limit, i + 1, cache)
    take = values[i] + _knapsack(values, weights, weight_limit - weights[i], i + 1, cache)

    res = max(dont_take, take)
    cache[key] = res
    return res


def driver():
    res = knapsack([5, 4, 9], [6, 1, 15], 20) # -> 13
    print(res)
