"""
Lowest Common Ancestor of a Binary Tree  (LeetCode #236, Medium)

Problem
    Given a binary tree and two nodes p and q in it, return their lowest common
    ancestor: the deepest node that has both as descendants (a node counts as a
    descendant of itself).

Example
    tree [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1 -> 3
    same tree, p = 5, q = 4 -> 5

Approach
    Post-order DFS. Return the node if it's p or q. If the left and right
    recursive calls both return something, p and q are split across this node,
    so it's the LCA. Otherwise pass up whichever side found something.
    (For a BST, LeetCode #235, just walk down comparing values.)

Complexity
    Time O(n), Space O(h)
"""
from typing import Optional

from common.structures import TreeNode, build_tree, find_node


def lowest_common_ancestor(root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    if root is None or root is p or root is q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left or right


def test_lowest_common_ancestor():
    root = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    lca = lambda a, b: lowest_common_ancestor(root, find_node(root, a), find_node(root, b)).val
    assert lca(5, 1) == 3
    assert lca(5, 4) == 5
    assert lca(7, 4) == 2
    assert lca(6, 8) == 3
