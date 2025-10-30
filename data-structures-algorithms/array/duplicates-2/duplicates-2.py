

def has_duplicates_2(nums, k):
    hash_map = {}

    for index,value in enumerate(nums):
        if value in hash_map:
            return True

        hash_map[value] = index

        hash_map[value] = index
        if len(hash_map)>k:
            iterator = iter(hash_map)
            first_ele = next(iterator)
            del hash_map[first_ele]

    return False



# Test Case 1: Should return True (duplicate within distance)
nums1 = [1, 2, 3, 1]
k1 = 3
print(has_duplicates_2(nums1, k1))  # Expected: True
# Explanation: 1 at index 0 and 3, distance = 3 <= k

# Test Case 2: Should return True (adjacent duplicates)
nums2 = [1, 0, 1, 1]
k2 = 1
print(has_duplicates_2(nums2, k2))  # Expected: True
# Explanation: 1 at index 2 and 3, distance = 1 <= k

# Test Case 3: Should return False (duplicates too far)
nums3 = [1, 2, 3, 1, 2, 3]
k3 = 2
print(has_duplicates_2(nums3, k3))  # Expected: False
# Explanation: All duplicates are more than 2 apart

# Test Case 4: Should return True (same values)
nums4 = [99, 99]
k4 = 2
print(has_duplicates_2(nums4, k4))  # Expected: True
# Explanation: Adjacent duplicates

# Test Case 5: Should return False (no duplicates)
nums5 = [1, 2, 3, 4, 5]
k5 = 10
print(has_duplicates_2(nums5, k5))  # Expected: False
# Explanation: All elements are unique

# Test Case 6: Should return True (multiple same values)
nums6 = [1, 1, 1, 1]
k6 = 1
print(has_duplicates_2(nums6, k6))  # Expected: True
# Explanation: All 1s are adjacent

# Test Case 7: Should return False (k = 0)
nums7 = [1, 2, 3, 1]
k7 = 0
print(has_duplicates_2(nums7, k7))  # Expected: False
# Explanation: k=0 means duplicates must be at same index (impossible)

# Test Case 8: Should return True (large k)
nums8 = [1, 2, 3, 4, 5, 1]
k8 = 100
print(has_duplicates_2(nums8, k8))  # Expected: True
# Explanation: 1 at index 0 and 5, distance = 5 <= 100

# Test Case 9: Should return True (negative numbers)
nums9 = [-1, -2, -3, -1]
k9 = 3
print(has_duplicates_2(nums9, k9))  # Expected: True
# Explanation: -1 at index 0 and 3, distance = 3 <= k

# Test Case 10: Should return False (single element)
nums10 = [1]
k10 = 1
print(has_duplicates_2(nums10, k10))  # Expected: False
# Explanation: Only one element, no duplicates possible