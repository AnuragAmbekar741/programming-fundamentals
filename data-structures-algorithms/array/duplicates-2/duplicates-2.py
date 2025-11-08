def is_duplicate_in_range_simple(nums: list[int], k: int) -> bool:
    value_to_indices = {}
    for i,val in enumerate(nums):
        if val not in value_to_indices:
            value_to_indices[val] = []
        value_to_indices[val].append(i)
    
    for key,value in value_to_indices.items():
        if(len(value)>1):
            for i in range(len(value) - 1):
                difference = value[i + 1] - value[i]
                if difference <= k:
                    return True
    return False


print(is_duplicate_in_range_simple([1,2,3,4,1,2], 3))


def is_duplicate_in_range(nums:list[int],k:int):
    num_map = {}
    for index,value in enumerate(nums):
        if value in num_map:
            return True 
        num_map[index] = value
        if(len(num_map)>k):
            iterator = iter(num_map)
            first_ele = next(iterator)
            del num_map[first_ele]
            # del num_map[next(iter(num_map))]
    return False

