# You are building a new house in the neighborhood and want to choose a location
# so that the house is as close as possible to all other houses.

# Write a function, best_house_build, that takes in a grid.
# In the grid, 0's are empty spaces, 1's are houses, and 2's are trees.
# Your job is to find an empty space on the grid that has the shortest total travel distance to all houses.
# Your function should return a number that corresponds to this shortest total travel distance.
# If it is not possible to choose a location that is that is reachable by all houses, then return -1.

# When calculating the distance, you can only move up, down, left, or right. You may not pass through houses or trees.


from collections import deque, defaultdict
from math import inf


EMPTY_SPACE = 0
HOUSE = 1
TREE = 2


def best_house_build(grid):
    queue = deque()
    visited = defaultdict(set)
    total_distance = defaultdict(int)

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == HOUSE:
                # Queue: (pos, src)
                queue.append( ((r, c, 0), (r, c)) )
                visited[(r, c)].add((r, c))
    num_houses = len(queue)

    while queue:
        (r, c, dist), src = queue.popleft()
        deltas = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        for delta in deltas:
            dr, dc = delta
            new_pos = (dr, dc)
            dr_inbounds = dr >= 0 and dr < len(grid)
            dc_inbounds = dc >= 0 and dc < len(grid[0])
            if dr_inbounds and dc_inbounds and grid[dr][dc] == EMPTY_SPACE and src not in visited[new_pos]:
                new_dist = dist + 1
                visited[new_pos].add(src)
                queue.append( ((dr, dc, new_dist), src) )
                total_distance[new_pos] += new_dist

    min_distance = inf
    for pos in visited:
        if len(visited[pos]) == num_houses:
            if total_distance[pos] > 0 and total_distance[pos] < min_distance:
                min_distance = total_distance[pos]
    return min_distance if min_distance != inf else -1


def driver():
    grid = [
        [1,0,0,0,1],
        [2,0,1,0,0]
    ]
    res = best_house_build(grid) # -> 5
    print(res)

    grid = [
        [0,0,0,1,0,0,0,0],
        [0,1,0,0,0,2,0,0],
        [0,0,0,1,0,2,2,2],
        [0,0,0,0,0,2,0,0],
        [0,0,0,0,1,2,0,0]
    ]
    res = best_house_build(grid) # -> 8
    print(res)