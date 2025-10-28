# Contains Duplicate II

## Problem Statement

Given an integer array `nums` and an integer `k`, return `True` if there are **two distinct indices** `i` and `j` in the array such that:

- `nums[i] == nums[j]` (values are equal)
- `abs(i - j) <= k` (distance between indices is at most k)

Return `False` otherwise.

### Constraints:

- `1 ≤ nums.length ≤ 10^5`
- `-10^9 ≤ nums[i] ≤ 10^9`
- `0 ≤ k ≤ 10^5`

### Input:

- `nums`: An array of integers
- `k`: Maximum allowed distance between duplicate indices

### Output:

- Return `True` if there exist duplicates within distance k, `False` otherwise

---

## Examples

### Example 1:

**Input:**
