def count_smileys(arr):
    s = 0
    for i in arr:

        if len(i) > 2:
            if i[0] in ':;':
                if i[1] in '-~':
                    if i[2] in ')D':
                        s += 1

        if len(i) == 2:
            if i[0] in ':;':
                if i[1] in ')D':
                    s += 1
    return s