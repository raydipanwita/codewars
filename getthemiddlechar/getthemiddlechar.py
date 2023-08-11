def get_middle(s):
    l = len(s) # to check the len of the string
    if l == 1: # to rule out if the string is of 1 char
        return (s[0])
    if l % 2 == 0: # to rule out if the string is even
        l1 = int(l/2) # to find out the middle of the full string of even char
        l2 = l1 - 1 # as the index starts at 0 and for even strings we need 2 middle char
        return (s[l2])+(s[l1])
    else: # for rest odd string
        l3 = int((l - 1)/2) # if we deduct 1 from len of string and then divide by 2 we will get the middle char
        return (s[l3])