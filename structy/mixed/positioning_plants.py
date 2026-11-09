# You've been hired to plant flowers in a garden with n different positions.
# There are m different flower types.
# The prices of flower types vary depending on which position they are planted.
# Your bosses are picky, they tell you to never plant two of the same flower type right next to each other.
# What is the minimum cost we need to plant a flower in each position of the garden?

# Write a function, positioning_plants, that takes in a 2D list with dimensions n * m.
# Each row of the list represents the costs of the flower types at that position.
# This means that costs[i][j] represents the cost of planting flower type j at position i.
# For example:

# Given these costs,
# costs = [
#   [4, 3, 7],
#   [6, 1, 9],
#   [2, 5, 3]
# ]

# The costs of plants at position 1 are $6, $1, and $9.
# The cost of planting flower type 0 at position 1 is $6.
# The cost of planting flower type 2 at position 1 is $9.

# The function should return the minimum cost of planting flowers without placing the same flower type in adjacent positions.


from math import inf


def positioning_plants(costs):
    return _positioning_plants(costs, 0, None, {})


def _positioning_plants(costs: list[list[int]], pos: int, last_plant_idx: int, cache: dict):
    key = (pos, last_plant_idx)
    if key in cache:
        return cache[key]
    if pos == len(costs):
        return 0
    min_cost = inf
    for plant_type_idx, plant_cost in enumerate(costs[pos]):
        if plant_type_idx != last_plant_idx:
            min_cost = min(min_cost, plant_cost + _positioning_plants(costs, pos + 1, plant_type_idx, cache))
    cache[key] = min_cost
    return min_cost


def driver():
    res = positioning_plants([
        [4, 3, 7],
        [6, 1, 9],
        [2, 5, 3]
    ]) # -> 7, by doing 4 + 1 + 2.
    print(res)

    res = positioning_plants([
        [12, 14, 50, 12, 13],
        [6, 3, 20, 3, 16],
        [24, 12, 7, 2, 74],
        [4, 80, 45, 3, 100],
        [104, 13, 5, 14, 3],
        [38, 19, 7, 6, 24],
        [1, 20, 1, 2, 31],
        [13, 12, 5, 13, 9],
        [60, 32, 20, 3, 2],
        [24, 12, 7, 2, 42],
        [4, 80, 44, 1, 23],
        [104, 13, 5, 14, 28],
        [38, 19, 76, 6, 12],
        [12, 23, 12, 20, 13],
        [1, 3, 1, 1, 50],
        [1, 2, 12, 5, 36],
        [6, 2, 3, 12, 20],
        [4, 6, 4, 11, 15],
    ]) # -> 75
    print(res)
