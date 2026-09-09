from collections import deque

def closest_carrot(grid: list[list[str]], starting_row: int, starting_col: int):
    if grid[starting_row][starting_col] == 'X':
        return -1

    if grid[starting_row][starting_col] == 'C':
        return 0

    visited = set((starting_row, starting_col))
    queue = deque([(starting_row, starting_col, 0)])
    while queue:
        row, col, distance = queue.popleft()
        if grid[row][col] == 'C':
            return distance
        directions = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
        for r1, c1 in directions:
            if r1 >= 0 and c1 >= 0 and r1 < len(grid) and c1 < len(grid[0]) and (r1, c1) not in visited and grid[r1][c1] != 'X':                
                queue.append((r1, c1, distance + 1))
                visited.add((r1, c1))
    return -1

def closest_carrot_2(grid: list[list[str]], starting_row: int, starting_col: int):
    if grid[starting_row][starting_col] == 'X':
        return -1

    if grid[starting_row][starting_col] == 'C':
        return 0

    visited = set((starting_row, starting_col))
    queue = deque([(starting_row, starting_col, 0)])
    while queue:
        row, col, distance = queue.popleft()
        if grid[row][col] == 'C':
            return distance
        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dr, dc in deltas:
            r = dr + row
            c = dc + col
            if r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0]) and grid[r][c] != 'X' and (r, c) not in visited:
                queue.append((r, c, distance + 1))
                visited.add((r, c))
    return -1

def driver():
    grid = [
        ['O', 'O', 'O', 'O', 'O'],
        ['O', 'X', 'O', 'O', 'O'],
        ['O', 'X', 'X', 'O', 'O'],
        ['O', 'X', 'C', 'O', 'O'],
        ['O', 'X', 'X', 'O', 'O'],
        ['C', 'O', 'O', 'O', 'O'],
    ]

    res = closest_carrot_2(grid, 0, 0) # -> 5
    print(res)
