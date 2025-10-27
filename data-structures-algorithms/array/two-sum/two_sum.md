# Two Sum Problem

## Problem Statement

Given an array of integers `nums` and an integer target `k`, return the **indices** of the two numbers in the array such that they add up to the target `k`.

### Constraints:

- You may assume that each input would have **exactly one solution**
- You **cannot** use the same element twice
- You can return the answer in any order

### Input:

- `nums`: An array of `n` integers where `2 ≤ n ≤ 10^4`
- `k`: An integer target value where `-10^9 ≤ k ≤ 10^9`
- Each element in `nums` is an integer where `-10^9 ≤ nums[i] ≤ 10^9`

### Output:

- Return a list/array containing two indices `[index1, index2]` where `nums[index1] + nums[index2] == k`

---

## Examples

### Example 1:

**Input:**

```
nums = [2, 7, 11, 15]
k = 9
```

**Output:**

```
[0, 1]
```

**Explanation:** Because `nums[0] + nums[1] == 2 + 7 == 9`, we return `[0, 1]`

---

### Example 2:

**Input:**

```
nums = [3, 2, 4]
k = 6
```

**Output:**

```
[1, 2]
```

**Explanation:** Because `nums[1] + nums[2] == 2 + 4 == 6`, we return `[1, 2]`

---

### Example 3:

**Input:**

```
nums = [3, 3]
k = 6
```

**Output:**

```
[0, 1]
```

**Explanation:** Because `nums[0] + nums[1] == 3 + 3 == 6`, we return `[0, 1]`

---

### Example 4:

**Input:**

```
nums = [-1, -2, -3, -4, -5]
k = -8
```

**Output:**

```
[2, 4]
```

**Explanation:** Because `nums[2] + nums[4] == -3 + (-5) == -8`, we return `[2, 4]`

---

## Your Task

Implement a function with the following signature:

```python
def two_sum(nums: list[int], k: int) -> list[int]:
    """
    Find two indices in nums such that nums[i] + nums[j] = k

    Args:
        nums: List of integers
        k: Target sum

    Returns:
        List containing two indices [i, j] where nums[i] + nums[j] = k
    """
    # Your code here
    pass
```

---

## Follow-up Questions to Consider:

1. What is the time complexity of your solution?
2. What is the space complexity of your solution?
3. Can you solve it in O(n) time?
4. What data structure would be most efficient for this problem?
