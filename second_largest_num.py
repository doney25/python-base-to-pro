def sec_lnum(arr):
   
    if len(arr) < 2:
        return None

    first = second = float('-inf')

    for num in arr:
        if num > first: 
            second = first
            first = num
        elif first > num > second:
            second = num

    return second
print(sec_lnum([1, 2, 3, 4, 5]))
