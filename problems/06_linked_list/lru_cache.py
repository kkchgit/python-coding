"""
LRU Cache  (LeetCode #146, Medium)

Problem
    Design a fixed-capacity cache with get(key) and put(key, value), both O(1).
    When full, inserting a new key evicts the least recently used key.
    get returns -1 for missing keys.

Approach
    Hash map from key to node in a doubly linked list ordered by recency.
    Sentinel head/tail nodes remove edge cases. Accessing a key moves its node
    to the front; eviction removes the node just before the tail.
    (In Python, collections.OrderedDict with move_to_end does the same job, but
    interviewers usually want to see the linked list.)

Complexity
    Time O(1) per operation, Space O(capacity)
"""


class _Node:
    __slots__ = ("key", "val", "prev", "next")

    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head, self.tail = _Node(), _Node()  # head.next = most recent
        self.head.next, self.tail.prev = self.tail, self.head

    def _remove(self, node: _Node) -> None:
        node.prev.next, node.next.prev = node.next, node.prev

    def _add_front(self, node: _Node) -> None:
        node.prev, node.next = self.head, self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        node = self.map.get(key)
        if not node:
            return -1
        self._remove(node)
        self._add_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self._remove(self.map[key])
        node = _Node(key, value)
        self.map[key] = node
        self._add_front(node)
        if len(self.map) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.key]


def test_lru_cache():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)          # evicts key 2
    assert cache.get(2) == -1
    cache.put(4, 4)          # evicts key 1
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4


def test_lru_update_existing():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(1, 10)         # refreshes key 1
    cache.put(3, 3)          # evicts key 2
    assert cache.get(1) == 10
    assert cache.get(2) == -1
