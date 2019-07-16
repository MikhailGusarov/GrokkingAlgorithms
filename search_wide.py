def search_wide(graph: dict, start: str, end: str) -> str:
    """Поиск в ширину"""
    arr = [start]  # очередь
    arr_search = []  # список просмотренных вершин графа
    while arr:
        step = arr.pop(0)  # взять из очереди первый элемент
        if step == end:
            return 'Е бой'
        if step not in arr_search:  # если элемента в arr_search нет
            arr_search.append(step)  # добавить эллемент в список
            arr += graph[step]  # добавить всех соседей в очередь
    return 'Говно'  # если очередь опустела, то пути нет


graph_initial = {
    'A': ['B', 'F'],
    'B': ['A', 'F', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'E'],
    'E': ['F', 'D'],
    'F': ['A', 'B', 'G', 'E'],
    'G': ['F', 'H'],
    'H': ['G']}
