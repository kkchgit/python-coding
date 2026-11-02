"""
Minimum Window Substring  (LeetCode #76, Hard)

Problem
    Return the shortest substring of `s` that contains every character of `t`
    (including duplicates). Return "" if no such window exists.

Example
    s = "ADOBECODEBANC", t = "ABC" -> "BANC"

Approach
    Expand the right edge until the window covers all of t (tracked with a
    `missing` counter so the check is O(1)). Then shrink from the left as far
    as possible while still covering t, recording the best window. Repeat.

Complexity
    Time O(|s| + |t|), Space O(|t|)
"""
from collections import Counter


def min_window(s: str, t: str) -> str:
    if not t or not s:
        return ""
    need = Counter(t)
    missing = len(t)
    left = 0
    best_start, best_len = 0, float("inf")

    for right, ch in enumerate(s):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1

        while missing == 0:
            if right - left + 1 < best_len:
                best_start, best_len = left, right - left + 1
            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            left += 1

    return "" if best_len == float("inf") else s[best_start:best_start + best_len]


def test_min_window():
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window("a", "a") == "a"
    assert min_window("a", "aa") == ""
    assert min_window("aaflslflsldkalskaaa", "aaa") == "aaa"
