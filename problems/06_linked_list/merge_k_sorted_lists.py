"""
Merge k Sorted Lists  (LeetCode #23, Hard)

Problem
    Merge k sorted linked lists into one sorted linked list.

Example
    [1->4->5, 1->3->4, 2->6] -> 1->1->2->3->4->4->5->6

Approach
    Min-heap holding the current front node of each list. Pop the smallest,
    append it, and push its successor. The index in each tuple breaks ties so
    Python never has to compare ListNode objects.

Complexity
    Time O(N log k) for N total nodes, Space O(k)
"""
import heapq
from typing import List, Optional

from common.structures import ListNode, build_list, to_list


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
    heapq.heapify(heap)
    dummy = tail = ListNode()
    while heap:
        _, i, node = heapq.heappop(heap)
        tail.next = tail = node
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next


def test_merge_k_lists():
    lists = [build_list([1, 4, 5]), build_list([1, 3, 4]), build_list([2, 6])]
    assert to_list(merge_k_lists(lists)) == [1, 1, 2, 3, 4, 4, 5, 6]
    assert merge_k_lists([]) is None
    assert merge_k_lists([None]) is None
