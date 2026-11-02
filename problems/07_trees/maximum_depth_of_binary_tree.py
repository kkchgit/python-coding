"""
Maximum Depth of Binary Tree  (LeetCode #104, Easy)

Problem
    Return the number of nodes on the longest path from the root to a leaf.

Example
    [3,9,20,null,null,15,7] -> 3

Approach
    Recursive DFS: depth = 1 + max(depth(left), depth(right)), with an empty
    tree having depth 0. An iterative BFS that counts levels works too and
    avoids recursion limits on very deep trees.

Complexity
    Time O(n), Space O(h) where h is the tree height
"""
from collections import deque
from typing import Optional

from common.structures import TreeNode, build_tree


def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def max_depth_bfs(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    depth, queue = 0, deque([root])
    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return depth


def test_max_depth():
    for fn in (max_depth, max_depth_bfs):
        assert fn(build_tree([3, 9, 20, None, None, 15, 7])) == 3
        assert fn(build_tree([1, None, 2])) == 2
        assert fn(None) == 0
