def longest_consec(strarr, k):
    n = len(strarr)
    if n == 0 or k > n or k <= 0:
        return ""

    max_len = 0
    max_str = ""

    for i in range(n-k+1):
        current_str = "".join(strarr[i:i+k])
        current_len = len(current_str)
        if current_len > max_len:
            max_len = current_len
            max_str = current_str

    return max_str