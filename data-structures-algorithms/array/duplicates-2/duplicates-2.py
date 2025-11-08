def is_duplicate_in_range1(nums: list[int], k: int) -> bool:
    value_to_indices = {}
    
    for i in range(len(nums)):
        value = nums[i]
        if value not in value_to_indices:
            value_to_indices[value] = []
        value_to_indices[value].append(i)
    
    for value, indices in value_to_indices.items():
        if len(indices) > 1:
            for i in range(len(indices) - 1):
                difference = indices[i + 1] - indices[i]
                if difference <= k:
                    return True
    
    return False
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

print(is_duplicate_in_range([1,2,1,4,1,6], 1))