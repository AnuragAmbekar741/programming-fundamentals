# Contains Duplicate Problem

## Problem Statement

Given an integer array `nums`, return `True` if any value appears **at least twice** in the array, and return `False` if every element is distinct.

### Constraints:

- `1 ≤ nums.length ≤ 10^5`
- `-10^9 ≤ nums[i] ≤ 10^9`

### Input:

- `nums`: An array of integers

### Output:

- Return `True` if array contains duplicates, `False` otherwise

---

## Examples

### Example 1:

**Input:**

```
nums = [1, 2, 3, 1]
```

**Output:**

```
True
```

**Explanation:** The element `1` appears at index 0 and index 3.

---

### Example 2:

**Input:**

```
nums = [1, 2, 3, 4]
```

**Output:**

```
False
```

**Explanation:** All elements are distinct.

---

### Example 3:

**Input:**

```
nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
```

**Output:**

```
True
```

**Explanation:** Multiple duplicates exist (1, 3, 4, 2 all appear more than once).

---

## Your Task

Implement a function with the following signature:

```python
def contains_duplicate(nums: list[int]) -> bool:
    """
    Check if array contains any duplicate elements

    Args:
        nums: List of integers

    Returns:
        True if duplicates exist, False otherwise
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
5. Can you solve it without using extra space? (Hint: sorting)

---

# Bonus Challenges

## Challenge 1: Find All Duplicates

Given an integer array `nums`, return a list of all elements that appear **more than once** in the array.

### Example:

**Input:**

```
nums = [4, 3, 2, 7, 8, 2, 3, 1]
```

**Output:**

```
[2, 3]
```

```python
def find_duplicates(nums: list[int]) -> list[int]:
    """
    Find all elements that appear more than once

    Args:
        nums: List of integers

    Returns:
        List of duplicate elements
    """
    # Your code here
    pass
```

---

## Challenge 2: Find Duplicate Number

Given an array `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive. There is only **one repeated number** in `nums`, return this repeated number.

### Constraints:

- You must solve it **without** modifying the array
- Use only **constant extra space** O(1)

### Example:

**Input:**

```
nums = [1, 3, 4, 2, 2]
```

**Output:**

```
2
```

```python
def find_duplicate(nums: list[int]) -> int:
    """
    Find the one duplicate number in array of range [1, n]

    Args:
        nums: List of integers in range [1, n]

    Returns:
        The duplicate number
    """
    # Your code here
    pass
```

---

## Challenge 3: Count Duplicates

Given an array `nums`, return a dictionary where keys are elements that appear more than once, and values are the count of their occurrences.

### Example:

**Input:**

```
nums = [1, 2, 3, 1, 2, 1]
```

**Output:**

```
{1: 3, 2: 2}
```

```python
def count_duplicates(nums: list[int]) -> dict[int, int]:
    """
    Count occurrences of duplicate elements

    Args:
        nums: List of integers

    Returns:
        Dictionary mapping duplicate elements to their counts
    """
    # Your code here
    pass
```

---

## Challenge 4: Remove Duplicates In-Place

Given an integer array `nums` sorted in **non-decreasing order**, remove duplicates **in-place** such that each unique element appears only once. Return the number of unique elements.

### Constraints:

- Modify the array in-place
- Don't use extra space for another array

### Example:

**Input:**

```
nums = [1, 1, 2, 2, 3, 4, 4]
```

**Output:**

```
4
```

**Explanation:**

- Function returns `4` (number of unique elements)
- First 4 elements of `nums` should be `[1, 2, 3, 4]`

```python
def remove_duplicates(nums: list[int]) -> int:
    """
    Remove duplicates in-place from sorted array

    Args:
        nums: Sorted list of integers (modified in-place)

    Returns:
        Number of unique elements
    """
    # Your code here
    pass
```

---

## Tips for Solving:

- Hash sets are very useful for detecting duplicates
- Consider time vs space trade-offs
- Sorting can sometimes help, but changes time complexity
- For in-place solutions, consider two-pointer technique
- Python's `Counter` from collections module can help with counting
