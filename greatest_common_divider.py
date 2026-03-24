def gcd(a, b): 
    """
    Возвращает НОД двух чисел с помощью алгоритма Евклида.
    """
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

def gcd_range(arr, L, R):
    """
    Возвращает gcd(arr[L], arr[L+1], ..., arr[R]).
    Индексация: 0..len(arr)-1.
    Бросает IndexError при некорректном диапазоне.
    """
    if L < 0 or R >= len(arr) or L > R:
        raise IndexError("Invalid range")
    g = 0
    for i in range(L, R + 1):
        g = gcd(g, abs(arr[i]))
        if g == 1:
            return 1
    return g
