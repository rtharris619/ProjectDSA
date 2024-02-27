# LeetCode 332 - Hard
from typing import List


def find_itinerary(tickets: List[List[str]]) -> List[str]:
    result = ["JFK"]

    adj = {src: [] for src, dst in tickets}

    tickets.sort()

    for src, dst in tickets:
        adj[src].append(dst)

    def dfs(source: str):
        if len(result) == len(tickets) + 1:
            return True
        if source not in adj:
            return False

        neighbors = list(adj[source])
        for i, v in enumerate(neighbors):
            result.append(v)
            adj[source].pop(i)
            if dfs(v):
                return True
            result.pop()
            adj[source].insert(i, v)
        return False

    dfs("JFK")

    return result


def solve():
    tickets1 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]

    tickets2 = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    result2 = find_itinerary(tickets2)
    print(result2)
