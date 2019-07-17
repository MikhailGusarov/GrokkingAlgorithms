def max_val(arr: list) -> int:
    """Максимальное значение рекурсивным способом"""
    if arr:  # проверка на пустой массив
        return None
    if len(arr) == 1:  # точка выхода
        return arr[0]
    pop_val = arr.pop()
    max_val_elem = max_val(arr)
    if pop_val > max_val_elem:
        return pop_val
    return max_val_elem

