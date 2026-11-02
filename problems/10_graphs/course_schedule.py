"""
Course Schedule  (LeetCode #207, Medium)

Problem
    There are `num_courses` courses labeled 0..n-1. Each pair [a, b] in
    `prerequisites` means you must take b before a. Can you finish them all?

Example
    2, [[1, 0]] -> True;   2, [[1, 0], [0, 1]] -> False

Approach
    It's possible exactly when the prerequisite graph has no cycle. Kahn's
    algorithm (BFS topological sort): start with courses that have no
    prerequisites, "take" them and decrement their dependents' in-degrees,
    queueing any that hit zero. If we take every course, there's no cycle.
    Returning `order` instead solves Course Schedule II (#210).

Complexity
    Time O(V + E), Space O(V + E)
"""
from collections import deque
from typing import List


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    graph = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

    queue = deque(i for i in range(num_courses) if indegree[i] == 0)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for nxt in graph[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    return len(order) == num_courses


def test_can_finish():
    assert can_finish(2, [[1, 0]])
    assert not can_finish(2, [[1, 0], [0, 1]])
    assert can_finish(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    assert not can_finish(3, [[0, 1], [1, 2], [2, 0]])
    assert can_finish(1, [])
