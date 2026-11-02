"""
Serialize and Deserialize Binary Tree  (LeetCode #297, Hard)

Problem
    Design functions that turn a binary tree into a string and rebuild the
    exact same tree from that string.

Example
    [1,2,3,null,null,4,5] -> "1,2,#,#,3,4,#,#,5,#,#" -> same tree

Approach
    Pre-order DFS writing "#" for empty children. Because every null is
    recorded, the string is unambiguous: deserialization reads tokens in the
    same pre-order, building a node and then its left and right subtrees.

Complexity
    Time O(n), Space O(n)
"""
from typing import Optional

from common.structures import TreeNode, build_tree, tree_to_list


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        out = []

        def dfs(node):
            if not node:
                out.append("#")
                return
            out.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(out)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        tokens = iter(data.split(","))

        def build():
            tok = next(tokens)
            if tok == "#":
                return None
            node = TreeNode(int(tok))
            node.left = build()
            node.right = build()
            return node

        return build()


def test_codec_round_trip():
    codec = Codec()
    for values in ([1, 2, 3, None, None, 4, 5], [], [1], [-1, None, -2, None, -3]):
        root = build_tree(values)
        assert tree_to_list(codec.deserialize(codec.serialize(root))) == values


def test_codec_format():
    assert Codec().serialize(build_tree([1, 2, 3, None, None, 4, 5])) == "1,2,#,#,3,4,#,#,5,#,#"
