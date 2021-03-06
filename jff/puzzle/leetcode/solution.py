from heapq import merge
from typing import List


def remove_duplicates(nums: List[int]) -> int:
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            del nums[i]
        else:
            i += 1
    return len(nums)


def is_palindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]


def median_of_two_sorted_arrays(x: List[int], y: List[int]) -> float:
    merged = list(merge(x, y))
    length = len(merged)
    middle = length >> 1

    print(length)
    print(middle)

    if length % 2 == 1:
        return merged[middle]
    else:
        return (merged[middle - 1] + merged[middle]) / 2


def get_no_zero_integers(n: int) -> List[int]:
    """returns the converted integer into the sum of two no-zero integers"""

    def get_sum(minuend: int, deductible: int) -> List[int]:
        if '0' in str(minuend) or '0' in str(deductible):
            return get_sum(minuend - 1, deductible + 1)
        else:
            return [minuend, deductible]

    return get_sum(n - 1, 1)


def minimum_flips(a: int, b: int, c: int) -> int:
    """returns the minimum flips to make a or b equal to c"""

    def process(x, y, z):
        if x | y == z:
            return 0
        return 1 if z else x + y

    count: int = 0
    while a or b or c:
        count += process(a & 1, b & 1, c & 1)
        a >>= 1
        b >>= 1
        c >>= 1
    return count


def build_an_array_with_stack_operations(target: List[int], n: int) -> List[str]:
    """
    Given an array target and an integer n. In each iteration, you will read a number from  list = {1,2,3..., n}.

    Build the target array using the following operations:

    Push: Read a new element from the beginning list, and push it in the array.
    Pop: delete the last element of the array.
    If the target array is already built, stop reading more elements.
    """
    PUSH_OPERATION: str = "Push"
    POP_OPERATION: str = "Pop"
    result: List[str] = []
    index: int = 1
    for element in target:
        if element == index:
            result.append(PUSH_OPERATION)
            index = element + 1
        else:
            while index < element:
                result.append(PUSH_OPERATION)
                result.append(POP_OPERATION)
                index += 1
            result.append(PUSH_OPERATION)
            index = element + 1

    return result
