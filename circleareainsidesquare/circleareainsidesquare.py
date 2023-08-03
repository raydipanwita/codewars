def square_area_to_circle(size):
    #from area of a square we can figure out sides of a square as Area of square = s * s
    import math
    x = math.sqrt(size) # to find out side of a square as side of a square will be the diameter of the circle
    y = x / 2 #to find out radius of the circle, side or diameter by 2
    return ((math.pi) * (y * y ))