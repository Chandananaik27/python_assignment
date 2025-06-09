import logging

logging.basicConfig(level=logging.DEBUG, format="%(message)s")

def string_formatting(k: int) -> str:
    if k < 1:
        return ""

    de = [str(i) for i in range(1, k + 1)]
    oc = [oct(i)[2:] for i in range(1, k + 1)]
    he = [hex(i)[2:].upper() for i in range(1, k + 1)]
    bi = [bin(i)[2:] for i in range(1, k + 1)]

    width = len(bi[-1])  # Width based on largest binary number
    res = ""
    for i in range(k):
        res += f"{de[i]:>{width}} {oc[i]:>{width}} {he[i]:>{width}} {bi[i]:>{width}}\n"

    logging.debug(res)
    return res
