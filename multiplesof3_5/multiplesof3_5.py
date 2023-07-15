def solution(number):
    sum = 0
    x = 1
    while x < (number):
        if x % 3 == 0 or x % 5 == 0:
            sum = sum + x
        x +=1
        
    return(sum) 
    pass