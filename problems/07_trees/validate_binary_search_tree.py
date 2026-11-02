"""
Validate Binary Search Tree  (LeetCode #98, Medium)

Problem
    Decide whether a binary tree is a valid BST: every node's left subtree has
    only smaller values, its right subtree only larger values, recursively.

Example
    [2,1,3] -> True;  [5,1,4,null,null,3,6] -> False

Approach
    Pass down the open interval (low, high) each node must fall inside. Going
    left tightens the upper bound; going right tightens the lower bound.
    Common mistake: only comparing a node with its direct children misses
    violations deeper in the tree (see the second test).

Complexity
    Time O(n), Space O(h)
"""
from typing import Optional

from common.structures import TreeNode, build_tree


def is_valid_bst(root: Optional[TreeNode],
                 low: float = float("-inf"), high: float = float("inf")) -> bool:
    if not root:
        return True
    if not (low < root.val < high):
        return False
    return (is_valid_bst(root.left, low, root.val)
            and is_valid_bst(root.right, root.val, high))


def test_is_valid_bst():
    assert is_valid_bst(build_tree([2, 1, 3]))
    assert not is_valid_bst(build_tree([5, 1, 4, None, None, 3, 6]))
    assert not is_valid_bst(build_tree([5, 4, 6, None, None, 3, 7]))  # 3 sits under 5's right
    assert not is_valid_bst(build_tree([2, 2, 2]))
    assert is_valid_bst(None)
