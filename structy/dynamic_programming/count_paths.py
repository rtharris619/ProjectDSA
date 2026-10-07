def count_paths(grid):
    return _count_paths(grid, 0, 0, {})

def _count_paths(grid, row, col, memo):
    pos = (row, col)
    if pos in memo:
        return memo[pos]
    if row == len(grid) or col == len(grid[0]):
        return 0
    if grid[row][col] == "X":
        return 0
    if row == len(grid) - 1 and col == len(grid[0]) - 1:
        return 1
    
    down_count = _count_paths(grid, row + 1, col, memo)
    right_count = _count_paths(grid, row, col + 1, memo)

    memo[pos] = down_count + right_count
    return memo[pos]

def driver():
    grid = [
        ["O", "O", "X"],
        ["O", "O", "O"],
        ["O", "O", "O"],
    ]
    res = count_paths(grid) # -> 5
    print(res)