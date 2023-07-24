def likes(names):
    # your code here
    size = len(names)
    size1 = size - 2
    
    if size == 0:
        return ("no one likes this")
    elif size == 1:
        return names[0] + " " + "likes this"
    elif size == 2:
        return names[0] + " and " + names[1] + " " + "like this"
    elif size == 3:
        return names[0] + ", " + names[1] + " and " + names[2] + " " + "like this"
    else:
        return names[0] + ", " + names[1] + " and " + str(size1) + " " + "others like this"
        