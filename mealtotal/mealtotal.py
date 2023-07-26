def calculate_total(subtotal, tax, tip):
    
    taxamount = float((subtotal * tax)/100)
    tipamount = float((subtotal * tip)/100)
    total = round(float(subtotal + tipamount + taxamount),2)
    return total
    pass