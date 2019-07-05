def binary_search(arr, val)-> int:
    """Бинарный поиск, возвращает номер val в списке arr"""
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = int((low + high) / 2)
        guess = arr[mid]
        if guess == val:
            return mid
        if guess < val:
            low = mid + 1
        else:
            high = mid - 1
    return None
    
