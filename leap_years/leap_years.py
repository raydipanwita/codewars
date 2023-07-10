def isLeapYear(year):
    if year%4 == 0 and year%100 !=0:
        return True#your code here. Try to do it in one line.
    elif year %400 == 0:
        return True
    else:
        return False #True/False