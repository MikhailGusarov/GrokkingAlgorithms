def algorithm_dijkstra(graph: dict,costs: dict,parent: dict, start: str, end: str)-> str:
    """Алгоритм Дейкстры"""
    processed = []
    pass

graph = {'S': {'A': 6, 'B': 2},
         'A': {'E': 1},
         'B': {'A': 3, 'E': 5},
         'E': {}}

costs = {'A': 6, 'B': 2, 'E': float("inf")}

parent = {'A': 'S', 'B': 'S': None}
