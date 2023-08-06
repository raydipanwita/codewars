def circle_area(r):
    import math
    if type(r) != int:      # to rule out any strings input
        return False
    elif r <= 0:            # to rule out any numbers less than 0
        return False
    else:
        return round(((math.pi) * (r * r)), 2) # round to round the result and 2 to get result upto 2 decimal places
    pass    