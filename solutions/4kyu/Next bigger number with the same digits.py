def next_bigger(n):
    l = []
    flag = False
    for i in str(n):
        l.append(int(i))
    for i in range(len(l) - 1, 0, -1):
        if l[i - 1] < l[i]:
            smallest = i
            for j in range(i + 1, len(l)):
                if l[j] > l[i - 1] and l[j] < l[smallest]:
                    smallest = j

            l[i - 1], l[smallest] = l[smallest], l[i - 1]

            l[i:] = sorted(l[i:])

            flag = True

            break

    if not flag:
        return -1

    return int(''.join(map(str, l)))