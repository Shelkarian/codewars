def solution(s):
    res = ''
    for i in s:
        if i.islower():
            res += i
        else:
            res += f' {i}'
    return res