def binary_search(arr: list, val: int) -> int:
    """Бинарный поиск, возвращает номер val в списке arr (рекурсивный случай)"""

    mid = int((len(arr)-1)/2)  # Берем середину списка
    guess = arr[mid]
    if guess != val and len(arr) == 1:  # если в массиве 1 эллемент и это не val, то вернуть None
        return None
    if guess == val:  # если нашли значение, вернуть индекс
        return mid
    """если значение больше, то возвращаем значение рекурсии по второй половине списка + текущее положение mid +1"""
    if guess < val:
        return mid + 1 + binary_search(arr[mid+1:], val)
    else:  # иначе, возвращаем рекурсию первой половины списка
        return binary_search(arr[:mid], val)
