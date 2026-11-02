"""
Word Ladder  (LeetCode #127, Hard)

Problem
    Transform `begin` into `end` by changing one letter at a time, where every
    intermediate word must be in `word_list`. Return the number of words in the
    shortest such sequence (including both ends), or 0 if impossible.

Example
    begin = "hit", end = "cog",
    word_list = ["hot","dot","dog","lot","log","cog"] -> 5  (hit-hot-dot-dog-cog)

Approach
    Shortest path in an unweighted graph, so BFS. To find neighbors fast, map
    wildcard patterns ("h*t", "*it", ...) to the words matching them; two
    words are neighbors exactly when they share a pattern. Clearing a pattern
    after using it keeps the search from revisiting it.

Complexity
    Time O(N * L^2) for N words of length L, Space O(N * L^2)
"""
from collections import defaultdict, deque
from typing import List


def ladder_length(begin: str, end: str, word_list: List[str]) -> int:
    words = set(word_list)
    if end not in words:
        return 0
    L = len(begin)
    patterns = defaultdict(list)
    for w in words | {begin}:
        for i in range(L):
            patterns[w[:i] + "*" + w[i + 1:]].append(w)

    visited = {begin}
    queue = deque([(begin, 1)])
    while queue:
        word, steps = queue.popleft()
        if word == end:
            return steps
        for i in range(L):
            key = word[:i] + "*" + word[i + 1:]
            for nxt in patterns[key]:
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, steps + 1))
            patterns[key] = []
    return 0


def test_ladder_length():
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    assert ladder_length("hit", "cog", words) == 5
    assert ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
    assert ladder_length("a", "c", ["a", "b", "c"]) == 2
