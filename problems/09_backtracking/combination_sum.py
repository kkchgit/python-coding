"""
Combination Sum  (LeetCode #39, Medium)

Problem
    Given distinct positive `candidates` and a `target`, return every unique
    combination of candidates that sums to target. Each candidate may be used
    any number of times.

Example
    candidates = [2, 3, 6, 7], target = 7 -> [[2, 2, 3], [7]]

Approach
    Backtracking over sorted candidates. Recurse with the same index (reuse
    allowed) and the reduced remainder. Starting each loop at the current
    index avoids permutations of the same combination; sorting lets us stop
    as soon as a candidate exceeds what's left.

Complexity
    Time exponential, roughly O(n^(target/min)), Space O(target/min) recursion
"""
from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    candidates = sorted(candidates)
    result, path = [], []

    def backtrack(start: int, remaining: int) -> None:
        if remaining == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            c = candidates[i]
            if c > remaining:
                break
            path.append(c)
            backtrack(i, remaining - c)
            path.pop()

    backtrack(0, target)
    return result


def test_combination_sum():
    assert combination_sum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert combination_sum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert combination_sum([2], 1) == []
