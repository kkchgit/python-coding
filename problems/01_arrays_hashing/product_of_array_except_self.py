"""
Product of Array Except Self  (LeetCode #238, Medium)

Problem
    Return a list where position i holds the product of every element of `nums`
    except nums[i]. Do it in O(n) without using division.

Example
    [1, 2, 3, 4] -> [24, 12, 8, 6]

Approach
    answer[i] = (product of everything left of i) * (product of everything
    right of i). First pass fills prefix products into the output; second pass
    walks right-to-left multiplying in a running suffix product.

Complexity
    Time O(n), Space O(1) extra (output list doesn't count)
"""
from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [1] * n
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    return result


def test_product_except_self():
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert product_except_self([2, 3]) == [3, 2]
