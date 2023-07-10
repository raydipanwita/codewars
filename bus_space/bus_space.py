def enough(cap, on, wait):
    space_left = cap - on 
    if space_left >= wait:
        return 0
    else:
        return wait - space_left