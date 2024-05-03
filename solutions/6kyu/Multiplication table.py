def multiplication_table(size):
    r = []
    for i in range(1, size+1):
        r.append([])
        for j in range(1, size+1):
            r[-1].append(i*j)
    return r