def pig_it(text):
    li = [i for i in text.split()]

    res = ''
    for i in li:
        if i.isalpha():

            res += i[1:] + i[0]
            res += 'ay '
        else:
            res += i
    return res.strip()