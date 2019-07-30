def algorithm_dijkstra(graph: dict, start: str, end: str) -> None:
    """Алгоритм Дейкстры"""
    processed = []  # проверенные вершины
    costs = graph[start].copy()  # цены на тек. проверке
    parent = {i: start for i in graph[start].keys()}  # родители на тек. проверку
    if end not in costs.keys():
        costs[end] = float("inf")
        parent[end] = None
    min_in_dict(costs, processed)


def min_in_dict(costs: dict, processed: list) -> str:
    min_val = float('inf')
    for k, v in costs.items():
        if k not in processed and v < min_val:
            res = k
            min_val = v
    return res



graph1 = {'S': {'A': 6, 'B': 2},
          'A': {'E': 1},
          'B': {'A': 3, 'E': 5},
          'E': {}}

algorithm_dijkstra(graph1, 'S', 'E')
