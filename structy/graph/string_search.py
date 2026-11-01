# Write a function, string_search, that takes in a grid of letters and a string as arguments.
# The function should return a boolean indicating whether or not the string can be found in the grid as a path
# by connecting horizontal or vertical positions. 
# The path can begin at any position, but you cannot reuse a position more than once in the path.

# You can assume that all letters are lowercase and alphabetic.

def string_search(grid, s):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == s[0]:
                if dfs(grid, row, col, s, 0, set()):
                    return True
    return False


def dfs(grid: list[list[str]], row: int, col: int, s: str, i: int, visited: set):
    if i == len(s):
        return True
    
    pos = (row, col)
    if pos in visited:
        return False
    if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]):
        return False
    if grid[row][col] != s[i]:
        return False

    visited.add(pos)
    result = (dfs(grid, row - 1, col, s, i + 1, visited) or
            dfs(grid, row + 1, col, s, i + 1, visited) or
            dfs(grid, row, col - 1, s, i + 1, visited) or
            dfs(grid, row, col + 1, s, i + 1, visited))
    visited.remove(pos)
    return result


def string_search_improved(grid, s):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == s[0]:
                if dfs_improved(grid, row, col, s, 0):
                    return True
    return False


def dfs_improved(grid: list[list[str]], row: int, col: int, s: str, i: int):
    if not (row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])):
        return False
    
    if grid[row][col] != s[i]:
        return False

    if i == len(s) - 1:
        return True

    temp = grid[row][col]
    grid[row][col] = "#"
    result = (dfs_improved(grid, row - 1, col, s, i + 1) or
            dfs_improved(grid, row + 1, col, s, i + 1) or
            dfs_improved(grid, row, col - 1, s, i + 1) or
            dfs_improved(grid, row, col + 1, s, i + 1))
    grid[row][col] = temp
    return result


def driver():
    grid = [
        ['e', 'y', 'h', 'i', 'j'],
        ['q', 'x', 'e', 'r', 'p'],
        ['r', 'o', 'l', 'l', 'n'],
        ['p', 'r', 'x', 'o', 'h'],
        ['a', 'a', 'm', 'c', 'm']
    ]
    res = string_search(grid, 'hello') # -> True
    print(res)

    grid = [ 
        [ 'f', 'd', 'i', 'e', 'l', 'u', 'j', 't', 'q', 'v', 'o', 'p' ], 
        [ 'o', 'p', 'b', 'e', 'm', 'w', 'm', 'l', 'h', 'j', 's', 'v' ], 
        [ 'g', 'b', 's', 'm', 'i', 'w', 'w', 'h', 'l', 'm', 'l', 'n' ], 
        [ 'a', 'l', 's', 'k', 'p', 'c', 't', 'u', 'v', 'b', 'c', 'm' ], 
        [ 'm', 't', 'c', 'k', 'e', 'n', 'r', 'b', 'a', 'z', 'l', 'c' ], 
        [ 'q', 'm', 'a', 'p', 'a', 'p', 'i', 'i', 'u', 't', 'z', 'z' ], 
        [ 'd', 'u', 'z', 'o', 'e', 'r', 'a', 't', 't', 'c', 'q', 'k' ], 
        [ 'f', 'u', 'z', 'g', 'c', 'i', 'k', 'v', 'o', 'f', 's', 'w' ], 
        [ 'p', 'h', 'u', 'i', 'k', 'c', 'v', 'v', 'h', 'q', 'v', 'i' ], 
        [ 'l', 'q', 'w', 'f', 'y', 'g', 'w', 'f', 'a', 'u', 'x', 'q' ] 
    ]
    res = string_search(grid, 'paprika') # -> True
    print(res)

    grid = [
        [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
        [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
        [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
        [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
        [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
        [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
        [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
        [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 'x', 'x' ],
        [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 'x', 'h' ],
    ]
    res = string_search(grid, 'ssssssssssh') # -> False
    print(res)

    grid = [
        ['a', 'o', 'o', 'o', 'o'],
        ['b', 'c', 'd', 'o', 'o'],
        ['c', 'f', 'e', 'o', 'o'],
        ['d', 'o', 'o', 'o', 'o'],
        ['o', 'o', 'o', 'o', 'o'],
    ]
    res = string_search(grid, 'abcdefc') # -> True
    print(res)
