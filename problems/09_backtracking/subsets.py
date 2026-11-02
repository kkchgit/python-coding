"""
Subsets  (LeetCode #78, Medium)

Problem
    Given a list of distinct integers, return every possible subset (the power
    set), without duplicates, in any order.

Example
    [1, 2, 3] -> [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]

Approach
    Backtracking: at each start index, record the current path as a subset,
    then try extending it with each later element and undo the choice after
    recursing. Only moving forward guarantees each subset appears once.

Complexity
    Time O(n * 2^n), Space O(n) recursion (plus output)
"""
from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    result, path = [], []

    def backtrack(start: int) -> None:
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()

    backtrack(0)
    return result


def test_subsets():
    assert sorted(subsets([1, 2, 3])) == sorted(
        [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])
    assert subsets([0]) == [[], [0]]
    assert len(subsets(list(range(10)))) == 1024
