"""
Word Break  (LeetCode #139, Medium)

Problem
    Return True if string `s` can be split into a sequence of one or more words
    from `word_dict` (words may be reused).

Example
    s = "applepenapple", word_dict = ["apple", "pen"] -> True

Approach
    dp[i] is True when the prefix s[:i] can be segmented. dp[0] = True (empty
    prefix). For each end i, look back only as far as the longest dictionary
    word: if some dp[j] is True and s[j:i] is a word, dp[i] is True.

Complexity
    Time O(n * W) where W is the longest word length (string slicing adds a
    factor of W), Space O(n + dictionary size)
"""
from typing import List


def word_break(s: str, word_dict: List[str]) -> bool:
    words = set(word_dict)
    max_len = max(map(len, words), default=0)
    dp = [True] + [False] * len(s)
    for i in range(1, len(s) + 1):
        for j in range(max(0, i - max_len), i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[len(s)]


def test_word_break():
    assert word_break("leetcode", ["leet", "code"])
    assert word_break("applepenapple", ["apple", "pen"])
    assert not word_break("catsandog", ["cats", "dog", "sand", "and", "cat"])
    assert not word_break("a", [])
