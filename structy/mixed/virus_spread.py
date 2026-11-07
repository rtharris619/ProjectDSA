# Oh no! There is a computer virus going around in our data center. 
# The virus spreads to adjacent computers.

# Write a function, virus_spread, that takes in a grid.
# In the grid, 0's are empty spaces, 1's are clean computers, and 2's are infected computers.
# Every hour, the virus spreads from infected computers to immediately adjacent clean computers.
# The virus can only spread to adjacent computers that are up, down, left, or right.

# The function should return the number of hours it will take for all computers to be infected.
# If it is impossible for all computers to become infected, then return -1.


from collections import deque
EMPTY_SPACE = 0
CLEAN_COMPUTER = 1
INFECTED_COMPUTER = 2


def virus_spread(grid):

    queue = deque([])
    visited = set()
    time = 0
    clean_computers = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == CLEAN_COMPUTER:
                clean_computers += 1
            if grid[row][col] == INFECTED_COMPUTER:
                visited.add((row, col))
                queue.append((row, col, 0))

    while queue:
        r, c, t = queue.popleft()
        time = t
        directions = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        for direction in directions:
            dr, dc = direction
            # if inbounds and its not a empty space
            if (dr >= 0 and dc >= 0 and dr < len(grid) and dc < len(grid[0])
                    and (dr, dc) not in visited
                    and grid[dr][dc] != EMPTY_SPACE
                ):
                clean_computers -= 1
                visited.add((dr, dc))
                queue.append((dr, dc, t + 1))
    
    return time if clean_computers == 0 else -1


def driver():
    grid = [
        [1,1,1],
        [0,1,0],
        [0,1,2]
    ]
    res = virus_spread(grid) # -> 4
    print(res)

    grid = [
        [1,0,1],
        [0,1,0],
        [0,1,2]
    ]
    res = virus_spread(grid) # -> -1
    print(res)

    grid = [
        [0,0,0,0,1,1,2],
        [0,1,1,1,1,1,0],
        [0,2,0,0,0,0,0]
    ]
    res = virus_spread(grid) # -> 3
    print(res)

    grid = [
        [2,1,1,1,1,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0],
        [0,0,0,1,1,0,1],
        [0,0,0,2,2,0,1],
        [0,0,0,0,0,0,1],
        [2,1,1,1,1,1,1]
    ]
    res = virus_spread(grid) # -> 9
    print(res)
