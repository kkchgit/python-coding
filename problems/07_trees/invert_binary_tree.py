"""
Invert Binary Tree  (LeetCode #226, Easy)

Problem
    Mirror a binary tree: swap every node's left and right children.

Example
    [4,2,7,1,3,6,9] -> [4,7,2,9,6,3,1]

Approach
    Recursively invert both subtrees and swap them. Any traversal order works
    as long as every node gets its children swapped once.

Complexity
    Time O(n), Space O(h)
"""
from typing import Optional

from common.structures import TreeNode, build_tree, tree_to_list


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root:
        root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


def test_invert_tree():
    assert tree_to_list(invert_tree(build_tree([4, 2, 7, 1, 3, 6, 9]))) == [4, 7, 2, 9, 6, 3, 1]
    assert tree_to_list(invert_tree(build_tree([2, 1, 3]))) == [2, 3, 1]
    assert invert_tree(None) is None
