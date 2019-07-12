def binary_search(arr, val)-> int:
    """Бинарный поиск, возвращает номер val в списке arr (рекурсивный случай)"""
    #Берем середину списка
    mid = int((len(arr)-1)/2)
    guess = arr[mid]
    #если в массиве 1 эллемент и это не val, то вернуть None
    if guess != val and len(arr) == 1:
        return None
    #если нашли значение, вернуть индекс
    if guess == val:
        return mid
    #если значение больше,
    #то возвращаем значение рекурсии по второй половине списка
    #+ текущее положение mid +1
    if guess < val:
        return mid + 1+ binary_search(arr[mid+1:], val)
    #иначе, возвращаем рекурсию первой половины списка
    else:
        return binary_search(arr[:mid], val)

    
