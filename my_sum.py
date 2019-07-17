def my_sum(arr: list) -> int:
    """Суммирует список рекурсивным способом"""
    if len(arr) == 1:
        return arr[0]
    return arr.pop() + my_sum(arr)
