def is_valid_state(state, n):
    return len(state) == n


# Where no queens can attack each other
def get_candidates(state, n):

    if not state:
        return range(n)

    # find the next position in the state to populate
    position = len(state)
    candidates = set(range(n))

    print(position, candidates)

    # prune down candidates that place the queen into attacks
    for row, col in enumerate(state):
        # discard the column index if it's occupied by a queen
        candidates.discard(col)
        dist = position - row
        # discard diagonals
        candidates.discard(col + dist)
        candidates.discard(col - dist)

    return candidates


def search(state, solutions, n):
    if is_valid_state(state, n):
        solutions.append(state.copy())
        return

    for candidate in get_candidates(state, n):
        state.append(candidate)
        search(state, solutions, n)
        state.pop()


def solve():
    n = 4
    solutions = []
    state = []
    search(state, solutions, n)
    # print(solutions)
