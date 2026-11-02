"""
Longest Repeating Character Replacement  (LeetCode #424, Medium)

Problem
    `s` contains uppercase letters. You may change at most `k` characters.
    Return the length of the longest substring that can be made of a single
    repeated letter.

Example
    s = "AABABBA", k = 1 -> 4

Approach
    A window is valid if (window length - count of its most common letter) <= k.
    Grow the window to the right; when it becomes invalid, slide the left edge
    forward by one. `max_freq` never needs to decrease: a smaller value can't
    produce a longer answer than one we've already recorded.

Complexity
    Time O(n), Space O(26)
"""
from collections import defaultdict


def character_replacement(s: str, k: int) -> int:
    counts = defaultdict(int)
    left = max_freq = best = 0
    for right, ch in enumerate(s):
        counts[ch] += 1
        max_freq = max(max_freq, counts[ch])
        if (right - left + 1) - max_freq > k:
            counts[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best


def test_character_replacement():
    assert character_replacement("ABAB", 2) == 4
    assert character_replacement("AABABBA", 1) == 4
    assert character_replacement("AAAA", 0) == 4
    assert character_replacement("ABCDE", 1) == 2
