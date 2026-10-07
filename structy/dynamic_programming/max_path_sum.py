from math import inf

def max_path_sum(grid):
    return _max_path_sum(grid, 0, 0, {})

def _max_path_sum(grid, row, col, memo):
    pos = (row, col)
    if pos in memo:
        return memo[pos]
    if row == len(grid) or col == len(grid[0]):
        return -inf
    if row == len(grid) - 1 and col == len(grid[0]) - 1:
        return grid[row][col]
    
    down_sum = _max_path_sum(grid, row + 1, col, memo)
    right_sum = _max_path_sum(grid, row, col + 1, memo)
    
    memo[pos] = max(down_sum, right_sum) + grid[row][col]
    return memo[pos]

def driver():
    grid = [
        [1, 3, 12],
        [5, 1, 1],
        [3, 6, 1],
    ]
    res = max_path_sum(grid) # -> 18
    print(res)