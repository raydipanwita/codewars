def odd_or_even(arr):
    Sum = sum(arr)
    if Sum == [0]:
        return "even"
    if Sum % 2 == 0:
        return "even"
    else:
        return "odd"
    pass    