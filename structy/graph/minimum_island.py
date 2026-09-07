from math import inf
from collections import deque

def dfs_rec(grid: list[list[str]], row: int, col: int, visited: set) -> int:
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
        return 0
    if (row, col) in visited or grid[row][col] == 'W':
        return 0
    visited.add((row, col))
    size = 1

    size += dfs_rec(grid, row - 1, col, visited)
    size += dfs_rec(grid, row + 1, col, visited)
    size += dfs_rec(grid, row, col - 1, visited)
    size += dfs_rec(grid, row, col + 1, visited)

    return size

def bfs(grid: list[list[str]], row: int, col: int, visited: set) -> int:
    if (row, col) in visited or grid[row][col] == 'W':
        return 0
    visited.add((row, col))
    size = 1
    queue = deque([(row, col)])
    while queue:
        r, c = queue.popleft()
        size += 1
        directions = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        for r1, c1 in directions:
            if r1 > 0 and c1 > 0 and r1 < len(grid) and c1 < len(grid[0]) and (r1, c1) not in visited and grid[r1][c1] == 'L':                
                queue.append((r1, c1))
                visited.add((r1, c1))
    return size

def minimum_island(grid):
    min_size = inf
    visited = set()

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'L':
                size = bfs(grid, row, col, visited)
                if size > 0 and size < min_size:
                    min_size = size

    return min_size

def driver():
    grid = [
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'W'],
        ['W', 'W', 'L', 'L', 'W'],
        ['L', 'W', 'W', 'L', 'L'],
        ['L', 'L', 'W', 'W', 'W'],
    ]

    res = minimum_island(grid) # -> 2
    print(res)