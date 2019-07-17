def algorithm_dijkstra(graph: dict, start: str, end: str)-> str:
    """Алгоритм Дейкстры"""
    processed = []  # проверенные вершины
    costs = graph[start].copy()  # цены на тек. проверке
    parent = {i: start for i in graph[start].keys()}  # родители на тек. проверку
    if end not in costs.keys():
        costs[end] = float("inf")
        parent[end] = None


graph = {'S': {'A': 6, 'B': 2},
         'A': {'E': 1},
         'B': {'A': 3, 'E': 5},
         'E': {}}

algorithm_dijkstra(graph, 'S', 'E')
