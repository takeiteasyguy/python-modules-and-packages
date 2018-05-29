def sum_while(l):
    n = 0
    s = 0
    while n < len(l):
        s += l[n]
        n += 1
    return s


def sum_for(l):
    s = 0
    for x in l:
        s += x
    return s