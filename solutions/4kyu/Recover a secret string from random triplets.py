def recoverSecret(triplets):
    letters = list(set([l for t in triplets for l in t]))
    for t in triplets * len(letters):
        for k in range(len(t)-1):
            a, b = letters.index(t[k]), letters.index(t[k+1])
            if(a > b): letters[b], letters[a] = letters[a], letters[b]
    return ''.join(letters)