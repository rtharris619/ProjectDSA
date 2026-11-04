# You are given the tolls for different highways.
# Each highway connects a pair of cities and has a particular cost that must be paid to use it.
# Each highway toll is a triplet (cityA, cityB, cost). Every highway can be traveled in either direction.
# Write a function that takes in highway tolls and two cities.
# The function should return the lowest cost required to travel between the two cities.
# You can assume that there exists at least one way to travel between the two cities.


from math import inf


def lowest_toll(highway_tolls, start_city, end_city):
    graph = convert_to_adjacency_list(highway_tolls)
    return min_path(graph, start_city, end_city, set())


def convert_to_adjacency_list(highway_tolls: list[tuple[str, str, float]]):
    # Hampton:  { Fairfax: 7.50, Roanaoke: 8.90 }
    # Fairfax:  { Hampton: 7.50, Manassas: 2.20 } ...
    graph = {}

    for tolls in highway_tolls:
        city_1, city_2, toll = tolls
        if city_1 not in graph:
            graph[city_1] = {}
        if city_2 not in graph:
            graph[city_2] = {}
        graph[city_1][city_2] = toll
        graph[city_2][city_1] = toll

    return graph


def min_path(graph: dict, start_city: str, end_city: str, visited: set):
    if start_city == end_city:
        return 0
    if start_city in visited:
        return inf
    
    visited.add(start_city)

    min_cost = inf
    for neighbor in graph[start_city]:
        cost = graph[start_city][neighbor]
        total_cost = cost + min_path(graph, neighbor, end_city, visited)
        min_cost = min(total_cost, min_cost)

    # backtrack
    visited.remove(start_city)

    return min_cost

def driver():
    highway_tolls = [
        ("Hampton", "Fairfax", 7.50),
        ("Roanoake", "Alexandria", 4.20),
        ("Alexandria", "Hampton", 14.50),
        ("Hampton", "Roanoake", 8.90),
        ("Alexandria", "Fairfax", 5.90),
        ("Hampton", "Manassas", 3.50),
        ("Fairfax", "Manassas", 2.20),
    ]
    res = lowest_toll(highway_tolls, "Alexandria", "Hampton") # -> 11.60
    print(res)
