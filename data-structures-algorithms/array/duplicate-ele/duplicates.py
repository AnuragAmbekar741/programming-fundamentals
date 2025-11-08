def is_duplicate(nums:list[int])->bool:
    num_map = {}
    for index,value in enumerate(nums):
        if value in num_map:
            return True
        else:
            num_map[index] = value
    return False


print(is_duplicate([1,2,3,4,1]))