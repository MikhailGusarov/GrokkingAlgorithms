def max_val(arr):
    """Максимальное значение рекурсивным способом"""
    #проверка на пустой массив
    if arr == []:
        return None
    #точка выхода
    if len(arr) == 1:
        return arr[0]
    pop_val = arr.pop()
    max_val_elem = max_val(arr)
    if pop_val > max_val_elem:
        return pop_val
    return max_val_elem
        
