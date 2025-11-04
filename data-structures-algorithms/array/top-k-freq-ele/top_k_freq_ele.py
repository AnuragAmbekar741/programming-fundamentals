def top_k_freq_ele2(nums:list[int],k:int)->list[int]:
    num_hash_map = {}
    result = []
    for num in nums:
        num_hash_map[num] = num_hash_map.get(num,0)+1
    sorted_num_freq = sorted(num_hash_map.items(),key=lambda x:x[1],reverse=True)
    return [item[0] for item in sorted_num_freq[:k]]

    return result[:k] if len(result) >= k else result
print(top_k_freq_ele2([1,2,2,3,1,2,1,4,5,3,6,7,7,7,4,4,4,4,4,4,2],2))

