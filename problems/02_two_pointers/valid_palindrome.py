"""
Valid Palindrome  (LeetCode #125, Easy)

Problem
    Decide whether a string reads the same forwards and backwards after
    lowercasing and ignoring every non-alphanumeric character.

Example
    "A man, a plan, a canal: Panama" -> True

Approach
    Two pointers from both ends. Skip characters that aren't letters/digits,
    compare the rest case-insensitively, and move inward. No copy of the string
    is needed.

Complexity
    Time O(n), Space O(1)
"""


def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


def test_is_palindrome():
    assert is_palindrome("A man, a plan, a canal: Panama")
    assert not is_palindrome("race a car")
    assert is_palindrome(" ")
    assert not is_palindrome("0P")
