import logging
logging.basicConfig(level=logging.DEBUG, format="%(message)s" )
def calculate_happiness():
    a = input()
    b = list(map(int, input().split(" ")))
    A = list(map(int, input().split(" ")))
    B = list(map(int, input().split(" ")))

    A.sort()
    B.sort()
    happiness = sum([A[i] == b[i] for i in range(len(A))]) - sum([B[i] == b[i] for i in range(len(B))])
    logging.debug(happiness)
    return abs(happiness)