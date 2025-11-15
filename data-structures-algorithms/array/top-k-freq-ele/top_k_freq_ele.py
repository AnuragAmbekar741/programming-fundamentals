def topKFrequent(nums: list[int], k: int) -> list[int]:
    result = {}
    for num in nums:
        if num in result:
            result[num]+=1
        else:
            result[num]=1
    sorted_keys = sorted(result.keys(), key=lambda k: result[k])
    return sorted_keys[-k:]

print(topKFrequent([1,22,3,4,5,3,1,3],3))