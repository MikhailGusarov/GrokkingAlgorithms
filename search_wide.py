def search_wide(graph, start, end):
    arr = [start]
    arr_search = []
    while arr:
        step = arr.pop(0)
        if step == end:
            return 'Е бой'
        if step not in arr_search:
            arr_search.append(step)
            arr += graph[step]
    return 'Говно'


graph_initial = {
    'A': ['B', 'F'],
    'B': ['A', 'F', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'E'],
    'E': ['F', 'D'],
    'F': ['A', 'B', 'G', 'E'],
    'G': ['F', 'H'],
    'H': ['G']}
