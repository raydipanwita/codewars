def add_length(str_):
    #your code here
    str_ = str_.split() # to split the string 
    
    text = []
    for x in str_:
        text.append(x + " " + str(len(x)))
    return text