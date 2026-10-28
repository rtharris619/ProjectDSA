# A knight and a pawn are on a chess board.
# Can you figure out the minimum number of moves required for the knight to travel to the same position of the pawn?
# On a single move, the knight can move in an "L" shape; two spaces in any direction, then one space in a perpendicular direction.
# This means that on a single move, a knight has eight possible positions it can move to.

# Write a function, knight_attack, that takes in 5 arguments:
# n, kr, kc, pr, pc
# n = the length of the chess board
# kr = the starting row of the knight
# kc = the starting column of the knight
# pr = the row of the pawn
# pc = the column of the pawn

# The function should return a number representing the minimum number of moves required for the knight to land on top of the pawn.
# The knight cannot move out-of-bounds of the board. You can assume that rows and columns are 0-indexed.
# This means that if n = 8, there are 8 rows and 8 columns numbered 0 to 7.
# If it is not possible for the knight to attack the pawn, then return None.

from collections import deque

def knight_attack(n, kr, kc, pr, pc):
    visited = set()
    visited.add((kr, kc))
    queue = deque([ (kr, kc, 0) ])
    while queue:
        r, c, moves = queue.popleft()
        if (r, c) == (pr, pc):
            return moves
        neighbors = get_knight_moves(n, r, c)
        for neighbor in neighbors:
            nr, nc = neighbor
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((nr, nc, moves + 1))
    return None

def get_knight_moves(n, r, c):
    positions = [
        (r + 1, c - 2),
        (r + 2, c - 1),
        (r - 2, c - 1),
        (r - 1, c - 2),
        (r + 2, c + 1),
        (r + 1, c + 2),
        (r - 1, c + 2),
        (r - 2, c + 1),
    ]
    valid_positions = []
    for pos in positions:
        dr, dc = pos
        if 0 <= dr < n and 0 <= dc < n:
            valid_positions.append(pos)
    return valid_positions

def knight_attack_old(n, kr, kc, pr, pc):
    grid = [[-1] * n for _ in range(n)]
    return bfs(grid, (kr, kc), (pr, pc))

def bfs(grid: list[list[int]], k_pos: tuple[int, int], p_pos: tuple[int, int]):
    queue = deque([(k_pos, 0)])
    visited = set([k_pos])
    while queue:
        (current_r, current_c), moves = queue.popleft()
        if (current_r, current_c) == p_pos:
            return moves
        right_up_1 =    (1, -2)
        right_up_2 =    (2, -1)
        left_up_1 =     (-2, -1)
        left_up_2 =     (-1, -2)
        right_down_1 =  (2, 1)
        right_down_2 =  (1, 2)
        left_down_1 =   (-1, 2)
        left_down_2 =   (-2, 1)        
        directions = [right_up_1, right_up_2, left_up_1, left_up_2, right_down_1, right_down_2, left_down_1, left_down_2]
        for dr, dc in directions:
            r, c = (current_r + dr, current_c + dc)
            if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]) and (r, c) not in visited: # in bounds and not yet visited
                visited.add((r, c))
                queue.append(((r, c), moves + 1))
    return None

def driver():
    res = knight_attack(8, 1, 1, 2, 2) # -> 2
    print(res)
