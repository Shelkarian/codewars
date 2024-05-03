def wave(people):
    res = []

    for i in range(len(people)):
        if people[i].isalpha():
            res.append(people[:i] + people[i].upper() + people[i+1:])
    return res