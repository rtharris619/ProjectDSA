def is_valid_move(maze, x, y, visited):
    rows, cols = len(maze), len(maze[0])
    return 0 <= x < rows and 0 <= y < cols and not visited[x][y] and maze[x][y] != '#'


def dfs(maze, x, y, visited, path):
    if is_valid_move(maze, x, y, visited):
        visited[x][y] = True
        path.append((x, y))

        # Explore all possible directions (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            dfs(maze, nx, ny, visited, path)

        path.pop()


def driver():
    # Example maze represented as a 2D array
    maze = [
        ['#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', '#', '#', '#', '#'],
    ]

    rows, cols = len(maze), len(maze[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    start_x, start_y = 1, 1  # Starting point in the maze
    dfs(maze, start_x, start_y, visited, [])

    total = 0
    for visits in visited:
        total += visits.count(True)
    print(total - 1)
