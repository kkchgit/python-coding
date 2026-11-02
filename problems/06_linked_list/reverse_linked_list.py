"""
Reverse Linked List  (LeetCode #206, Easy)

Problem
    Reverse a singly linked list and return the new head.

Example
    1 -> 2 -> 3 -> 4 -> 5  ->  5 -> 4 -> 3 -> 2 -> 1

Approach
    Walk the list keeping a `prev` pointer. For each node, save its next,
    point it back at prev, then advance. The recursive version is also worth
    knowing but uses O(n) stack space.

Complexity
    Time O(n), Space O(1)
"""
from typing import Optional

from common.structures import ListNode, build_list, to_list


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev


def reverse_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


def test_reverse_list():
    assert to_list(reverse_list(build_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert to_list(reverse_list(build_list([1, 2]))) == [2, 1]
    assert reverse_list(None) is None


def test_reverse_list_recursive():
    assert to_list(reverse_list_recursive(build_list([1, 2, 3]))) == [3, 2, 1]
