def get_sum(a, b):
    s = 0
    if a <= b:
        for i in range(a, b+1):
            s += i
    else:
        for i in range(b, a+1):
            s += i
    return s