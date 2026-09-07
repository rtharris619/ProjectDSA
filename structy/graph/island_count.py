from collections import deque

def dfs_rec(grid: list[list[str]], row: int, col: int, visited: set) -> bool:
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or (row, col) in visited or grid[row][col] == 'W':
        return False
    
    visited.add((row, col))

    directions = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]

    for direction in directions:
        r, c = direction
        dfs_rec(grid, r, c, visited)

    return True

def bfs(grid: list[list[str]], row: int, col: int, visited: set):
    if (row, col) in visited or grid[row][col] == 'W':
        return False
    visited.add((row, col))
    queue = deque([(row, col)])
    while queue:
        r, c = queue.popleft()
        directions = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        for direction in directions:
            r1, c1 = direction
            if r1 >= 0 and c1 >= 0 and r1 < len(grid) and c1 < len(grid[0]) and (r1, c1) not in visited and grid[r1][c1] == 'L':
                visited.add((r1, c1))
                queue.append((r1, c1))

    return True

def island_count(grid: list[list[str]]):
    count = 0
    visited = set()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'L' and bfs(grid, row, col, visited):
                count += 1

    return count

def driver():
    grid = [
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'W'],
        ['W', 'W', 'L', 'L', 'W'],
        ['L', 'W', 'W', 'L', 'L'],
        ['L', 'L', 'W', 'W', 'W'],
    ]
   
    res = island_count(grid) # -> 3
    print(res)