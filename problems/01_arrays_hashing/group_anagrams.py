"""
Group Anagrams  (LeetCode #49, Medium)

Problem
    Given a list of strings, group together the words that are anagrams of each
    other (same letters, possibly reordered). Groups may be returned in any order.

Example
    ["eat","tea","tan","ate","nat","bat"] -> [["eat","tea","ate"],["tan","nat"],["bat"]]

Approach
    Anagrams share the same letter counts. Use a 26-slot count tuple as a hash
    key (cheaper than sorting each word) and bucket words under that key.

Complexity
    Time O(n * k) where k is the max word length, Space O(n * k)
"""
from collections import defaultdict
from typing import List


def group_anagrams(words: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    for word in words:
        counts = [0] * 26
        for ch in word:
            counts[ord(ch) - ord("a")] += 1
        groups[tuple(counts)].append(word)
    return list(groups.values())


def _normalize(groups):
    return sorted(sorted(g) for g in groups)


def test_group_anagrams():
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert _normalize(result) == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
