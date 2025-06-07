import logging
logging.basicConfig(level=logging.DEBUG, format="%(message)s" )
from itertools import combinations

def iterator():

    n = list(range(1, int(input()) + 1))
    b = list(input().split(" "))
    indx = []
    for i in range(len(b)):
        if b[i] == "a":
            indx.append(i + 1)
    k = list(combinations(n, int(input())))
    out = 0
    for i in k:
        if any([j in i for j in indx]):
            out += 1
    logging.debug(out / len(list(k)))
    return out / len(list(k))
iterator()
