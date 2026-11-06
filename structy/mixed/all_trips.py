# You are given a list of bus routes, a starting station, and an ending station.
# A bus route is a pair of two stations (a, b) such that the bus travels from a to b, but not from b to a.

# Write a function that returns a list containing all possible trips we can make that travel
# from the starting station to the ending station.

# You can assume that there are no cycles in the bus routes.


def all_trips(routes, start_station, end_station):
    graph = convert_to_adjacency_list(routes)
    return [path[::-1] for path in _all_trips(graph, start_station, end_station) ]


def _all_trips(graph: dict[str, list[str]], start_station: str, end_station: str):
    if start_station == end_station:
        return [[start_station]]

    trips = []
    for neighbor in graph[start_station]:
        neighboring_trips = _all_trips(graph, neighbor, end_station)
        for neighbor_trip in neighboring_trips:
            # (Will be reversed later since it should be inserted at the beginning of the list)
            neighbor_trip.append(start_station)
            trips.append(neighbor_trip)
    return trips


def convert_to_adjacency_list(routes: list[tuple[str, str]]):
    graph: dict[str, list[str]] = {}
    for route in routes:
        a, b = route
        if a not in graph:
            graph[a] = []
        graph[a].append(b)
    return graph


def driver():
    routes = [
        ('brookdale', 'denton junction'),
        ('astor place', 'brookdale'),
        ('astor place', 'cony island'),
        ('astor place', 'denton junction'),
        ('cony island', 'denton junction')
    ]
    res = all_trips(routes, 'astor place', 'denton junction') # ->
    # [
    #   ['astor place', 'brookdale', 'denton junction'],
    #   ['astor place', 'cony island', 'denton junction'],
    #   ['astor place', 'denton junction']
    # ]
    print(res)
