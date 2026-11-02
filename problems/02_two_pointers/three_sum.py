"""
3Sum  (LeetCode #15, Medium)

Problem
    Find every unique triplet [a, b, c] in `nums` with a + b + c == 0. The
    result must not contain duplicate triplets.

Example
    [-1, 0, 1, 2, -1, -4] -> [[-1, -1, 2], [-1, 0, 1]]

Approach
    Sort, then fix the first element and solve "two sum on a sorted array" for
    the rest with two pointers. Skip repeated values for the fixed element and
    after each match to avoid duplicates. Stop early once the fixed value is
    positive (no way to reach zero).

Complexity
    Time O(n^2), Space O(1) extra besides sorting
"""
from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    nums = sorted(nums)
    result = []
    for i in range(len(nums) - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
    return result


def test_three_sum():
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert three_sum([0, 1, 1]) == []
    assert three_sum([0, 0, 0, 0]) == [[0, 0, 0]]
    assert three_sum([-2, 0, 1, 1, 2]) == [[-2, 0, 2], [-2, 1, 1]]
