def digital_root(n):
    # ...
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
        if len(str(total)) >= 2:
            total = digital_root(total)
    return total 