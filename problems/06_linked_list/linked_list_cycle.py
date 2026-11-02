"""
Linked List Cycle  (LeetCode #141, Easy)

Problem
    Return True if the linked list contains a cycle.

Example
    3 -> 2 -> 0 -> -4 -> (back to 2)  ->  True

Approach
    Floyd's tortoise and hare: a slow pointer moves 1 step, a fast pointer
    moves 2. If there's a cycle the fast one eventually laps the slow one; if
    not, fast reaches the end. Follow-up (LeetCode #142): after they meet,
    restart one pointer at head and step both by 1; they meet at the cycle
    start.

Complexity
    Time O(n), Space O(1)
"""
from typing import Optional

from common.structures import ListNode, build_list


def has_cycle(head: Optional[ListNode]) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def _make_cycle(values, pos):
    head = build_list(values)
    if pos < 0:
        return head
    nodes, node = [], head
    while node:
        nodes.append(node)
        node = node.next
    nodes[-1].next = nodes[pos]
    return head


def test_has_cycle():
    assert has_cycle(_make_cycle([3, 2, 0, -4], 1))
    assert has_cycle(_make_cycle([1, 2], 0))
    assert not has_cycle(_make_cycle([1], -1))
    assert not has_cycle(None)
