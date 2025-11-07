

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


nums1 = [1, 2, 3, 1]
k1 = 3
print(has_duplicates_2(nums1, k1))
