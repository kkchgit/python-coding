# Top 50 — Python

50 classic coding-interview problems frequently reported in FAANG-style interviews, grouped by the pattern that cracks them. Each problem is a single self-contained Python file with:

- a problem summary and example (in my own words, with the LeetCode number for reference)
- the approach and *why* it works
- time and space complexity
- a clean solution (sometimes two, e.g. recursive vs. iterative)
- pytest tests, including the edge cases interviewers like to probe

> The list is curated from widely shared interview prep lists (Blind 75, NeetCode-style roadmaps) rather than official company data. Companies don't publish their question banks, so treat "FAANG top 50" as "the 50 problems most worth knowing cold."

## Quick start

```bash
pip install -r requirements.txt
pytest                                   # run everything
pytest problems/07_trees                 # one pattern
pytest problems/01_arrays_hashing/two_sum.py -v
```

Requires Python 3.9+.

## How to practice with this repo

1. Pick a problem, read only the **Problem** and **Example** sections in the docstring.
2. Cover the rest, set a 25-minute timer, and solve it in a scratch file.
3. Paste your function over the solution and run that file's tests.
4. Then read the **Approach** section, even if you passed: the reasoning is what you'll be asked to explain out loud.
5. Re-solve the ones you missed a few days later.

## Problems

| # | Problem | Difficulty | Pattern / key idea | File |
|---|---------|-----------|--------------------|------|
| **Arrays & Hashing** |||||
| 1 | Two Sum (#1) | Easy | Hash map of seen values | [two_sum.py](problems/01_arrays_hashing/two_sum.py) |
| 2 | Group Anagrams (#49) | Medium | Letter-count tuple as key | [group_anagrams.py](problems/01_arrays_hashing/group_anagrams.py) |
| 3 | Top K Frequent Elements (#347) | Medium | Bucket sort by frequency | [top_k_frequent_elements.py](problems/01_arrays_hashing/top_k_frequent_elements.py) |
| 4 | Product of Array Except Self (#238) | Medium | Prefix × suffix products | [product_of_array_except_self.py](problems/01_arrays_hashing/product_of_array_except_self.py) |
| 5 | Longest Consecutive Sequence (#128) | Medium | Set, start only at run beginnings | [longest_consecutive_sequence.py](problems/01_arrays_hashing/longest_consecutive_sequence.py) |
| 6 | Subarray Sum Equals K (#560) | Medium | Prefix sums + count map | [subarray_sum_equals_k.py](problems/01_arrays_hashing/subarray_sum_equals_k.py) |
| **Two Pointers** |||||
| 7 | Valid Palindrome (#125) | Easy | Converging pointers | [valid_palindrome.py](problems/02_two_pointers/valid_palindrome.py) |
| 8 | 3Sum (#15) | Medium | Sort + two pointers, skip dupes | [three_sum.py](problems/02_two_pointers/three_sum.py) |
| 9 | Container With Most Water (#11) | Medium | Move the shorter side | [container_with_most_water.py](problems/02_two_pointers/container_with_most_water.py) |
| 10 | Trapping Rain Water (#42) | Hard | Running left/right max | [trapping_rain_water.py](problems/02_two_pointers/trapping_rain_water.py) |
| **Sliding Window** |||||
| 11 | Best Time to Buy and Sell Stock (#121) | Easy | Track min so far | [best_time_to_buy_and_sell_stock.py](problems/03_sliding_window/best_time_to_buy_and_sell_stock.py) |
| 12 | Longest Substring Without Repeating Characters (#3) | Medium | Last-seen index jump | [longest_substring_without_repeating_characters.py](problems/03_sliding_window/longest_substring_without_repeating_characters.py) |
| 13 | Longest Repeating Character Replacement (#424) | Medium | Window − max freq ≤ k | [longest_repeating_character_replacement.py](problems/03_sliding_window/longest_repeating_character_replacement.py) |
| 14 | Minimum Window Substring (#76) | Hard | Expand, then shrink | [minimum_window_substring.py](problems/03_sliding_window/minimum_window_substring.py) |
| **Stack** |||||
| 15 | Valid Parentheses (#20) | Easy | Matching stack | [valid_parentheses.py](problems/04_stack/valid_parentheses.py) |
| 16 | Min Stack (#155) | Medium | Store min alongside value | [min_stack.py](problems/04_stack/min_stack.py) |
| 17 | Daily Temperatures (#739) | Medium | Monotonic decreasing stack | [daily_temperatures.py](problems/04_stack/daily_temperatures.py) |
| 18 | Largest Rectangle in Histogram (#84) | Hard | Monotonic increasing stack | [largest_rectangle_in_histogram.py](problems/04_stack/largest_rectangle_in_histogram.py) |
| **Binary Search** |||||
| 19 | Search in Rotated Sorted Array (#33) | Medium | One half is always sorted | [search_in_rotated_sorted_array.py](problems/05_binary_search/search_in_rotated_sorted_array.py) |
| 20 | Find Minimum in Rotated Sorted Array (#153) | Medium | Compare mid to right end | [find_minimum_in_rotated_sorted_array.py](problems/05_binary_search/find_minimum_in_rotated_sorted_array.py) |
| 21 | Koko Eating Bananas (#875) | Medium | Binary search on the answer | [koko_eating_bananas.py](problems/05_binary_search/koko_eating_bananas.py) |
| 22 | Median of Two Sorted Arrays (#4) | Hard | Partition search | [median_of_two_sorted_arrays.py](problems/05_binary_search/median_of_two_sorted_arrays.py) |
| **Linked List** |||||
| 23 | Reverse Linked List (#206) | Easy | prev / curr / next | [reverse_linked_list.py](problems/06_linked_list/reverse_linked_list.py) |
| 24 | Merge Two Sorted Lists (#21) | Easy | Dummy head | [merge_two_sorted_lists.py](problems/06_linked_list/merge_two_sorted_lists.py) |
| 25 | Linked List Cycle (#141) | Easy | Floyd's fast/slow pointers | [linked_list_cycle.py](problems/06_linked_list/linked_list_cycle.py) |
| 26 | LRU Cache (#146) | Medium | Hash map + doubly linked list | [lru_cache.py](problems/06_linked_list/lru_cache.py) |
| 27 | Merge k Sorted Lists (#23) | Hard | Min-heap of list heads | [merge_k_sorted_lists.py](problems/06_linked_list/merge_k_sorted_lists.py) |
| **Trees** |||||
| 28 | Maximum Depth of Binary Tree (#104) | Easy | DFS / BFS levels | [maximum_depth_of_binary_tree.py](problems/07_trees/maximum_depth_of_binary_tree.py) |
| 29 | Invert Binary Tree (#226) | Easy | Swap children recursively | [invert_binary_tree.py](problems/07_trees/invert_binary_tree.py) |
| 30 | Binary Tree Level Order Traversal (#102) | Medium | BFS by level | [binary_tree_level_order_traversal.py](problems/07_trees/binary_tree_level_order_traversal.py) |
| 31 | Validate Binary Search Tree (#98) | Medium | Pass down (low, high) bounds | [validate_binary_search_tree.py](problems/07_trees/validate_binary_search_tree.py) |
| 32 | Lowest Common Ancestor of a Binary Tree (#236) | Medium | Post-order, split point | [lowest_common_ancestor_of_binary_tree.py](problems/07_trees/lowest_common_ancestor_of_binary_tree.py) |
| 33 | Serialize and Deserialize Binary Tree (#297) | Hard | Pre-order with null markers | [serialize_and_deserialize_binary_tree.py](problems/07_trees/serialize_and_deserialize_binary_tree.py) |
| **Heap / Priority Queue** |||||
| 34 | Kth Largest Element in an Array (#215) | Medium | Size-k min-heap | [kth_largest_element_in_array.py](problems/08_heap/kth_largest_element_in_array.py) |
| 35 | Find Median from Data Stream (#295) | Hard | Two heaps | [find_median_from_data_stream.py](problems/08_heap/find_median_from_data_stream.py) |
| **Backtracking** |||||
| 36 | Subsets (#78) | Medium | Choose / recurse / un-choose | [subsets.py](problems/09_backtracking/subsets.py) |
| 37 | Combination Sum (#39) | Medium | Reuse index, prune on sort | [combination_sum.py](problems/09_backtracking/combination_sum.py) |
| 38 | Word Search (#79) | Medium | Grid DFS with in-place marking | [word_search.py](problems/09_backtracking/word_search.py) |
| **Graphs** |||||
| 39 | Number of Islands (#200) | Medium | Flood fill | [number_of_islands.py](problems/10_graphs/number_of_islands.py) |
| 40 | Clone Graph (#133) | Medium | DFS + old→new map | [clone_graph.py](problems/10_graphs/clone_graph.py) |
| 41 | Course Schedule (#207) | Medium | Topological sort (Kahn) | [course_schedule.py](problems/10_graphs/course_schedule.py) |
| 42 | Rotting Oranges (#994) | Medium | Multi-source BFS | [rotting_oranges.py](problems/10_graphs/rotting_oranges.py) |
| 43 | Word Ladder (#127) | Hard | BFS with wildcard buckets | [word_ladder.py](problems/10_graphs/word_ladder.py) |
| **Dynamic Programming** |||||
| 44 | Climbing Stairs (#70) | Easy | Fibonacci recurrence | [climbing_stairs.py](problems/11_dynamic_programming/climbing_stairs.py) |
| 45 | House Robber (#198) | Medium | Rob or skip | [house_robber.py](problems/11_dynamic_programming/house_robber.py) |
| 46 | Coin Change (#322) | Medium | Unbounded knapsack | [coin_change.py](problems/11_dynamic_programming/coin_change.py) |
| 47 | Longest Increasing Subsequence (#300) | Medium | Patience sorting + bisect | [longest_increasing_subsequence.py](problems/11_dynamic_programming/longest_increasing_subsequence.py) |
| 48 | Word Break (#139) | Medium | Prefix segmentability | [word_break.py](problems/11_dynamic_programming/word_break.py) |
| **Intervals** |||||
| 49 | Merge Intervals (#56) | Medium | Sort by start, extend | [merge_intervals.py](problems/12_intervals/merge_intervals.py) |
| 50 | Meeting Rooms II (#253) | Medium | Min-heap of end times | [meeting_rooms_ii.py](problems/12_intervals/meeting_rooms_ii.py) |

**Difficulty mix:** 10 Easy · 32 Medium · 8 Hard

## Repo layout

```
python-coding/
├── common/structures.py   # ListNode, TreeNode and build/print helpers
├── problems/
│   ├── 01_arrays_hashing/
│   ├── ...
│   └── 12_intervals/
├── pytest.ini
└── requirements.txt
```

## Pattern cheat sheet

- **Need O(1) lookup of something you've seen?** Hash map / set.
- **Sorted input, or pairs/triplets?** Two pointers.
- **Contiguous substring/subarray with a constraint?** Sliding window (prefix sums if values can be negative).
- **"Next greater/smaller" element?** Monotonic stack.
- **Sorted or monotonic search space, or "minimum X such that..."?** Binary search.
- **Top/kth/median of a stream?** Heap.
- **All combinations/permutations?** Backtracking.
- **Shortest path in an unweighted graph or grid?** BFS. **Dependencies?** Topological sort.
- **Optimal value with overlapping subproblems?** DP: define the state, the recurrence, the base case.
- **Overlapping ranges?** Sort by start.
