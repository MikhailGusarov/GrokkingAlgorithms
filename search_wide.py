def search_wide(graph,start,end):
    arr=[start]
    arrSearch = []
    while arr:
        step = arr.pop(0)
        if step == end:
            return 'Е бой'
        if step not in arrSearch:
            arrSearch.append(step)
            arr += graph[step]
    return 'Говно'

graph = {'A': ['B', 'F'],
         'B':['A','F','C'],
         'C':['B','D'],
         'D':['C','E'],
         'E':['F','D'],
         'F':['A','B','G','E'],
         'G':['F','H'],
         'H':['G']}


