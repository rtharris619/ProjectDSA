# Write a function, breaking_boundaries, that takes in 5 arguments:
# A number of rows (m), a number of columns (n), a number of moves (k), a starting row (r), and a starting column (c).
# Say you were situated in a grid with dimensions m * n. If you had to start at position (r,c),
# in how many different ways could you move out of bounds if you could take at most k moves.
# A single move is moving one space up, down, left, or right.
# During a path you may revisit a position.

# For example:
# Given m, n, k, r, c:
# 3, 4, 2, 0, 0

# This input asks us to count the numbers of ways
# to move out of bounds in a 3 by 4 grid, starting at
# position (0, 0) if we could take at most 2 moves.

# The answer is 4 because of these 4 distinct ways:
#  1. left
#  2. up
#  3. right, up
#  4. down, left

# The function should return a number representing how many ways you can move out of bounds.


def breaking_boundaries(m, n, k, r, c):
    return _breaking_boundaries(m, n, k, r, c, {})


def _breaking_boundaries(m: int, n: int, k: int, r: int, c: int, cache: dict):
    key = (k, r, c)
    if key in cache:
        return cache[key]
    row_inbounds = r >= 0 and r < m
    col_inbounds = c >= 0 and c < n
    if not row_inbounds or not col_inbounds:
        return 1
    if k == 0:
        return 0

    ways = 0
    directions = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
    for direction in directions:
        new_r, new_c = direction
        ways += _breaking_boundaries(m, n, k - 1, new_r, new_c, cache)
    cache[key] = ways
    return ways


def driver():
    res = breaking_boundaries(3, 4, 2, 0, 0) # -> 4
    print(res)

    res = breaking_boundaries(3, 4, 3, 0, 0) # -> 11
    print(res)

    res = breaking_boundaries(4, 4, 5, 2, 1) # -> 160
    print(res)

    res = breaking_boundaries(6, 8, 16, 2, 1) # -> 137495089
    print(res)