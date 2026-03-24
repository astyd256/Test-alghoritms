def lowest_sum(arr):
    if len(arr) == 0:
        raise ValueError("array must contain at least two elements")
    if len(arr) == 1:
        return arr[0]
    
    if arr[0] <= arr[1]:
        min1, min2 = arr[0], arr[1]
    else:
        min1, min2 = arr[1], arr[0]
    
    for x in arr[2:]:
        if x < min2:
            min2 = x
            if x < min1:
                min2 = min1
                min1 = x
    return min1 + min2