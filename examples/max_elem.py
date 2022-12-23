def find_max(l):
    if len(l) == 0:
        raise ValueError("Empty list")
    max = l[0]
    for el in l[1:]:
        if max < el:
            max = el
    return max
