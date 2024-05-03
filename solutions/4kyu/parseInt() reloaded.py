def parse_int(string):
    keywords = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
        'eleven': 11,
        'twelve': 12,
        'thirteen': 13,
        'fourteen': 14,
        'fifteen': 15,
        'sixteen': 16,
        'seventeen': 17,
        'eighteen': 18,
        'nineteen': 19,
        'twenty': 20,
        'thirty': 30,
        'forty': 40,
        'fifty': 50,
        'sixty': 60,
        'seventy': 70,
        'eighty': 80,
        'ninety': 90,
    }
    mult = {
        'hundred': 100,
        'thousand': 1000,
        'million': 1000000
    }
    res = 0

    li = sum((i.split('-') for i in string.split()), [])

    for i in li:
        if i in keywords:
            res += keywords[i]
        if i in mult:
            match mult[i]:
                case 'million':
                    return 1000000
                case 'hundred':
                    res *= 100
                case _:
                    res += mult[i] * (res % mult[i]) - (res % mult[i])

    return res

