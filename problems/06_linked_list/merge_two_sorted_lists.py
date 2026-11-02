"""
Merge Two Sorted Lists  (LeetCode #21, Easy)

Problem
    Merge two sorted linked lists into one sorted list by splicing their nodes
    together, and return its head.

Example
    1->2->4 and 1->3->4  ->  1->1->2->3->4->4

Approach
    Dummy head plus a tail pointer. Repeatedly attach the smaller front node,
    then append whatever remains of the non-empty list.

Complexity
    Time O(m + n), Space O(1)
"""
from typing import Optional

from common.structures import ListNode, build_list, to_list


def merge_two_lists(a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
    dummy = tail = ListNode()
    while a and b:
        if a.val <= b.val:
            tail.next, a = a, a.next
        else:
            tail.next, b = b, b.next
        tail = tail.next
    tail.next = a or b
    return dummy.next


def test_merge_two_lists():
    merged = merge_two_lists(build_list([1, 2, 4]), build_list([1, 3, 4]))
    assert to_list(merged) == [1, 1, 2, 3, 4, 4]
    assert merge_two_lists(None, None) is None
    assert to_list(merge_two_lists(None, build_list([0]))) == [0]
