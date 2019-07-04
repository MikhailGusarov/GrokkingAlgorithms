def binary_search(arr, val)-> int:
    """Бинарный поиск, возвращает номер val в списке arr"""
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = int((low + high) / 2)
        guess = arr[mid]
        if guess < val:
            low = mid + 1
        elif guess > val:
            high = mid - 1
        else:
            return mid
    return
    
