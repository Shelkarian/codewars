def disemvowel(string_):
    for i in string_.lower():
        if i in ('a', 'o', 'e', 'i', 'u'):
            string_ = string_.replace(i.lower(), '')
            string_ = string_.replace(i.upper(), '')
    return string_