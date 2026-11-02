"""
Longest Substring Without Repeating Characters  (LeetCode #3, Medium)

Problem
    Return the length of the longest substring of `s` that has no repeated
    characters.

Example
    "abcabcbb" -> 3   ("abc")

Approach
    Sliding window. Remember the last index of each character. When the right
    edge hits a character already inside the window, jump the left edge just
    past that character's previous position.

Complexity
    Time O(n), Space O(min(n, alphabet size))
"""


def length_of_longest_substring(s: str) -> int:
    last_seen = {}
    left = best = 0
    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        best = max(best, right - left + 1)
    return best


def test_length_of_longest_substring():
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("") == 0
    assert length_of_longest_substring("abba") == 2
