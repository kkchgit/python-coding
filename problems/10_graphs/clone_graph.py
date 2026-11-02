"""
Clone Graph  (LeetCode #133, Medium)

Problem
    Given a node in a connected undirected graph, return a deep copy of the
    whole graph. Each node has a value and a list of neighbors.

Example
    adjacency [[2,4],[1,3],[2,4],[1,3]] (a 4-cycle) -> an identical but
    separate graph

Approach
    DFS with a map from original node to its copy. Create the copy the first
    time a node is seen, register it before visiting neighbors (that's what
    handles cycles), then clone each neighbor recursively.

Complexity
    Time O(V + E), Space O(V)
"""
from typing import Dict, List, Optional


class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List["Node"]] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Optional[Node]) -> Optional[Node]:
    copies: Dict[Node, Node] = {}

    def dfs(original: Node) -> Node:
        if original in copies:
            return copies[original]
        copy = Node(original.val)
        copies[original] = copy
        copy.neighbors = [dfs(n) for n in original.neighbors]
        return copy

    return dfs(node) if node else None


# ---------- test helpers ----------
def _build(adj: List[List[int]]) -> Optional[Node]:
    if not adj:
        return None
    nodes = [Node(i + 1) for i in range(len(adj))]
    for i, nbrs in enumerate(adj):
        nodes[i].neighbors = [nodes[j - 1] for j in nbrs]
    return nodes[0]


def _collect(node: Node) -> Dict[int, Node]:
    seen, stack = {}, [node]
    while stack:
        n = stack.pop()
        if n.val not in seen:
            seen[n.val] = n
            stack.extend(n.neighbors)
    return seen


def test_clone_graph():
    adj = [[2, 4], [1, 3], [2, 4], [1, 3]]
    original = _build(adj)
    clone = clone_graph(original)
    orig_nodes, clone_nodes = _collect(original), _collect(clone)
    assert sorted(clone_nodes) == [1, 2, 3, 4]
    for val, c in clone_nodes.items():
        assert c is not orig_nodes[val]                      # truly new objects
        assert [n.val for n in c.neighbors] == adj[val - 1]  # same structure
    assert clone_graph(None) is None


def test_clone_single_node():
    clone = clone_graph(Node(1))
    assert clone.val == 1 and clone.neighbors == []
