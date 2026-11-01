# Oh-no! You forgot the number combination that unlocks your safe.
# Luckily, you knew that you'd be forgetful so you previously wrote down a bunch of hints that can be used to determine
# the correct combination. 
# Each hint is a pair of numbers 'x, y' that indicates you must enter digit 'x' before 'y' (but not necessarily immediately before y).

# The keypad on the safe has digits 0-9. You can assume that the hints will generate exactly one working combination and that a digit
# can occur zero or one time in the answer.

# Write a function, safe_cracking, that takes in a list of hints as an argument and determines the combination 
# that will unlock the safe. The function should return a string representing the combination.

def safe_cracking(hints):
    graph = convert_to_graph(hints)

    # 1. init parent tracker
    num_parents = {}
    for node in graph:
        num_parents[node] = 0
    for node in graph:
        for child in graph[node]:
            num_parents[child] += 1

    # 2. go through the nodes from parent to child and get the order
    res = []
    ready = [node for node in num_parents if num_parents[node] == 0]
    while ready:
        current = ready.pop()
        res.append(current)
        for child in graph[current]:
            num_parents[child] -= 1
            if num_parents[child] == 0:
                ready.append(child)
    return "".join(map(str, res))


def convert_to_graph(hints: list[tuple[int, int]]):
    graph = {}
    for hint in hints:
        a, b = hint
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
    return graph


def driver():
    res = safe_cracking([
        (7, 1),
        (1, 8),
        (7, 8),
    ]) # -> '718'
    print(res)
