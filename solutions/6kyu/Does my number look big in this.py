def narcissistic(value):
    s = 0
    l = len(str(value))
    for i in str(value):
        s += int(i) ** l

    if value == s:
        return True
    else:
        return False