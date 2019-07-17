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


def search_wide2(graph: dict, start: str, end: str) -> list:
    """Поиск в ширину с выводом кратчайшего пути"""
    arr = [[start,start]]  # очередь (шаг пути)
    arr_search = []  # список просмотренных вершин графа
    arr_line = []  # список пройденных ребер 
    while arr:
        step = arr.pop(0)  # взять из очереди первый элемент
        if step[0] == end:
            arr_line.append(step)  # добавить последнее ребро
            end_step = end
            arr_res = [end]
            arr_line = {i[0]: i[1] for i in arr_line}  # преобразуем список в словарь
            while arr_line[end_step] != start:  # пока не дойдем до start
                arr_res.append(arr_line[end_step]) # добавляем шаги пути задом наперед
                end_step = arr_line[end_step]
            arr_res.append(start)
            arr_res.reverse()
            return arr_res
        if step[0] not in arr_search:  # если элемента в arr_search нет
            arr_search.append(step[0])  # добавить эллемент в список
            arr_line.append(step)  # добавить просмотренное ребро
            for i in graph[step[0]]:
                arr.append([i,step[0]])  # добавить всех соседей в очередь
    return 'Говно'  # если очередь опустела, то пути нет

graph_initial = {
    'A': ['B', 'F'],
    'B': ['A', 'F', 'C'],
    'C': ['B', 'D', 'K'],
    'D': ['C', 'E'],
    'E': ['F', 'D'],
    'F': ['A', 'B', 'G', 'E'],
    'G': ['F', 'H'],
    'H': ['G']}


start = 'A'
end = 'K'


search_wide(graph_initial, start, end)
print(search_wide2(graph_initial, start, end))
