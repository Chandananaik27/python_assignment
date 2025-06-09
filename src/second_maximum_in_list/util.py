import logging
from typing import Any

logging.basicConfig(level=logging.DEBUG, format="%(message)s")

def second_maximum(num: int, List: list[int]) -> Any:
    # Sort the list in ascending order
    for i in range(len(List)):
        for j in range(i + 1, len(List)):
            if List[i] > List[j]:
                List[i], List[j] = List[j], List[i]
    second_max = List[-2]  # Second last value after sorting
    logging.debug(f"The second largest value is {second_max}")
    return second_max
