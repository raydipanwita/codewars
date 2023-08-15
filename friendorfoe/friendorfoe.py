def friend(x):
    #Code
    results = []
    for elements in x:
        if len(elements) == 4: #to check if the length of the elements in list are 4 chars
            results.append(elements)
    return results