"""
Valid Parentheses  (LeetCode #20, Easy)

Problem
    A string contains only ()[]{} characters. Return True if every bracket is
    closed by the same type, in the correct order.

Example
    "()[]{}" -> True,  "(]" -> False

Approach
    Push opening brackets onto a stack. On a closing bracket, the top of the
    stack must be its partner. At the end the stack must be empty.

Complexity
    Time O(n), Space O(n)
"""


def is_valid(s: str) -> bool:
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)
    return not stack


def test_is_valid():
    assert is_valid("()")
    assert is_valid("()[]{}")
    assert not is_valid("(]")
    assert is_valid("{[]}")
    assert not is_valid("([)]")
    assert not is_valid("(")
    assert not is_valid("]")
