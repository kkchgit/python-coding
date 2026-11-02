"""
Min Stack  (LeetCode #155, Medium)

Problem
    Design a stack supporting push, pop, top and get_min, all in O(1) time.

Example
    push(-2), push(0), push(-3), get_min() -> -3, pop(), top() -> 0, get_min() -> -2

Approach
    Store each value together with the minimum of the stack at the time it was
    pushed. The current minimum is then always on top, and popping restores
    the previous minimum automatically.

Complexity
    Time O(1) per operation, Space O(n)
"""


class MinStack:
    def __init__(self):
        self._stack = []  # (value, min_so_far)

    def push(self, val: int) -> None:
        current_min = min(val, self._stack[-1][1]) if self._stack else val
        self._stack.append((val, current_min))

    def pop(self) -> None:
        self._stack.pop()

    def top(self) -> int:
        return self._stack[-1][0]

    def get_min(self) -> int:
        return self._stack[-1][1]


def test_min_stack():
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    assert s.get_min() == -3
    s.pop()
    assert s.top() == 0
    assert s.get_min() == -2


def test_min_stack_duplicates():
    s = MinStack()
    for v in (2, 1, 1):
        s.push(v)
    s.pop()
    assert s.get_min() == 1
    s.pop()
    assert s.get_min() == 2
