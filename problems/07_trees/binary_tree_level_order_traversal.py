"""
Binary Tree Level Order Traversal  (LeetCode #102, Medium)

Problem
    Return the tree's values level by level, left to right, as a list of lists.

Example
    [3,9,20,null,null,15,7] -> [[3], [9, 20], [15, 7]]

Approach
    BFS with a queue. At the start of each round, the queue holds exactly one
    level; process that many nodes, collecting their values and enqueueing
    their children.

Complexity
    Time O(n), Space O(w) where w is the widest level
"""
from collections import deque
from typing import List, Optional

from common.structures import TreeNode, build_tree


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


def test_level_order():
    assert level_order(build_tree([3, 9, 20, None, None, 15, 7])) == [[3], [9, 20], [15, 7]]
    assert level_order(build_tree([1])) == [[1]]
    assert level_order(None) == []
