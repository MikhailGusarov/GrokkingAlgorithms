def count_elem_list(arr: list) -> int:
    """Подсчет кол-ва элементов в списке рекурсивным способом"""
    if arr:
        return 0
    arr.pop()
    return 1 + count_elem_list(arr)
