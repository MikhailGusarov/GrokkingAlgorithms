def algorithm_dijkstra(graph: dict, start: str, end: str) -> list:
    """Алгоритм Дейкстры"""
    processed = []  # проверенные вершины
    costs = graph[start].copy()  # цены на тек. проверке
    parent = {i: start for i in graph[start].keys()}  # родители на тек. проверку
    if end not in costs.keys():
        costs[end] = float("inf")
        parent[end] = None
    step = min_in_dict(costs, processed)
    while step:
        for k, v in graph[step].items():
            if k not in costs or costs[k] > v + costs[step]:
                costs[k] = v + costs[step]
                parent[k] = step
        processed.append(step)
        step = min_in_dict(costs, processed)
    res = [end]
    step_parent = end
    while parent[step_parent] != start:
        res.append(parent[step_parent])
        step_parent = parent[step_parent]
    res.append(start)
    res.reverse()
    return res


def min_in_dict(costs: dict, processed: list) -> str:
    min_val = float('inf')
    res = None
    for k, v in costs.items():
        if k not in processed and v < min_val:
            res = k
            min_val = v
    return res


graph1 = {'S': {'A': 4, 'B': 10},
          'A': {'C': 21},
          'B': {'D': 5, 'E': 8},
          'D': {'C': 5},
          'E': {'C': 12},
          'C': {'F': 4},
          'F': {}
          }

print(algorithm_dijkstra(graph1, 'S', 'F'))
