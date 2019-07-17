def find_smallest(arr: list) -> int:
    """Поиск наименьшего числа"""
    smallest = arr[0]
    small_index = 0
    for i in range(1, len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
            small_index = i
    return small_index


def selection_sort(arr: list) -> list:
    """Выборочная сортировка"""
    sort_arr = []
    for i in range(0, len(arr)):
        sort_arr.append(arr.pop(find_smallest(arr)))
    return sort_arr


print(selection_sort([5, 4, 11, 21, 2, -5, 5]))
