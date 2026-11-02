"""
Climbing Stairs  (LeetCode #70, Easy)

Problem
    You climb a staircase of `n` steps taking 1 or 2 steps at a time. How many
    distinct ways can you reach the top?

Example
    n = 3 -> 3   (1+1+1, 1+2, 2+1)

Approach
    The last move onto step n came from n-1 or n-2, so ways(n) = ways(n-1) +
    ways(n-2): the Fibonacci recurrence. Only the last two values are needed,
    so keep two variables instead of a table. This is the gateway DP problem:
    define the state, find the recurrence, set base cases, compress space.

Complexity
    Time O(n), Space O(1)
"""


def climb_stairs(n: int) -> int:
    one, two = 1, 1  # ways to reach step i-1 and i-2
    for _ in range(n - 1):
        one, two = one + two, one
    return one


def test_climb_stairs():
    assert climb_stairs(1) == 1
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(5) == 8
    assert climb_stairs(45) == 1836311903
