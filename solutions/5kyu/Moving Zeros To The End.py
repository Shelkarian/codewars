def move_zeros(lst):
    l = lst.count(0)

    for i in range(l):
        lst.remove(0)
        lst.append(0)
    return lst