import logging

logging.basicConfig(level=logging.DEBUG, format="%(message)s")

def string_formatting():
    k = int(input("Enter the number: "))
    de = [str(i) for i in range(1, k + 1)]
    oc = [oct(i)[2:] for i in range(1, k + 1)]
    he = [hex(i)[2:].upper() for i in range(1, k + 1)]
    bi = [bin(i)[2:] for i in range(1, k + 1)]

    res = ""
    for i in range(k):
        res += f"{de[i]:>2}{' ':>5}{oc[i]:>3}{' ':>5}{he[i]:>3}{' ':>5}{bi[i]:>3}\n"
    logging.debug(res)
    return res