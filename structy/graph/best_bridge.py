from collections import deque

def inbounds(grid, row: int, col: int) -> bool:
    return row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0])

def directions(row: int, col: int):
    return [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]

def explore(grid: list[list[str]], row: int, col: int, island: set):
    island.add((row, col))
    queue = deque([(row, col)])
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions(r, c):
            if inbounds(grid, dr, dc) and (dr, dc) not in island and grid[dr][dc] == 'L':
                island.add((dr, dc))
                queue.append((dr, dc))

def explore_2(grid: list[list[str]], row: int, col: int, visited: set):
    if not inbounds(grid, row, col):
        return visited
    if grid[row][col] == 'W' or (row, col) in visited:
        return visited
    visited.add((row, col))
    for dr, dc in directions(row, col):
        explore_2(grid, dr, dc, visited)
    return visited

def find_next_island(grid: list[list[str]], first_island: set):
    visited = set()
    
    queue = deque([])
    for r, c in first_island:
        queue.append((r, c, 0))

    while queue:
        r, c, distance = queue.popleft()
        if grid[r][c] == 'L' and (r, c) not in first_island:
            return distance - 1
        for dr, dc in directions(r, c):
            if inbounds(grid, dr, dc) and (dr, dc) not in visited:
                visited.add((dr, dc))
                queue.append((dr, dc, distance + 1))

def best_bridge(grid: list[list[str]]) -> int:
    # 1. start at 0, 0 and find land
    # 2. explore first island completely (distances initialised to 0)
    # 3. fan out over the water from the island to the next island using BFS

    island = set()
    found = False
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'L':
                island = explore_2(grid, row, col, set())
                found = True
                break
        if found:
            break
   
    res = find_next_island(grid, island)
    return res

def driver():
    grid = [
        ["W", "W", "W", "L", "L"],
        ["L", "L", "W", "W", "L"],
        ["L", "L", "L", "W", "L"],
        ["W", "L", "W", "W", "W"],
        ["W", "W", "W", "W", "W"],
        ["W", "W", "W", "W", "W"],
    ]
    res = best_bridge(grid) # -> 1
    print(res)
