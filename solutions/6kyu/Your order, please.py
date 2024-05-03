def order(sentence):
    li = [i for i in sentence.split(' ')]
    res = []

    for i in range(len(li)):
        for _ in li:
            if str(i + 1) in _:
                res.append(li[li.index(_)])
    return ' '.join(res)