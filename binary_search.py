def binary_search(arr, val)-> int:
    """Бинарный поиск, возвращает номер val в списке arr"""
    low = 0
    high = len(arr) - 1
    
    mid = int((low + high) / 2)
    guess = arr[mid]
    while guess != val:
        mid = int((low + high) / 2)
        guess = arr[mid]
        if guess < val:
            low = mid + 1
        elif guess > val:
            high = mid - 1
    return mid
    
