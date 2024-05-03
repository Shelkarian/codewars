def find_it(seq):
    for i in seq:
        l = seq.count(i)
        if l % 2 != 0:
            return i