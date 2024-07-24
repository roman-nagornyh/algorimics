import typing
from typing import List
import math


def binary_search(seq: List[int], find_element: int) -> int:
    """Реализация алгоритма бинарного поиска"""

    result = -1
    low = 0

    if len(seq) == 0:
        return result

    high = len(seq) - 1
    seq.sort()

    while low <= high:
        # Непонятно, как работает эта строчка, мы остановились на стр 27
        mid = math.floor((low + high) / 2)
        guess = seq[mid]

        if guess == find_element:
            result = mid
            return result

        if guess > find_element:
            high = mid - 1
        else:
            low = mid + 1

    return result
