def top_k_freq_ele(nums:list[int],k:int)->list[int]:
    num_hash_map = {}
    result = []
    for num in nums:
        if num in num_hash_map:
            num_hash_map[num] += 1
            if num_hash_map[num] >= k:
                if(len(result) < k):
                    result.append(num)
                else:
                    return result
        else:
            num_hash_map[num] = 1
            if num_hash_map[num] >= k:
                if(len(result) < k):
                    result.append(num)
                else:
                    return result
    return result
print(top_k_freq_ele([1,2,2,3,1,2,1,4,5,3,6,7,7,7,4,4],2))


def top_k_freq_ele2(nums:list[int],k:int)->list[int]:
    num_hash_map = {}
    result = []
    for num in nums:
        num_hash_map[num] = num_hash_map.get(num,0)+1
    for num, freq in num_hash_map.items():
        if freq >= k:
            result.append(num)

    return result[:k] if len(result) >= k else result
print(top_k_freq_ele2([1,2,2,3,1,2,1,4,5,3,6,7,7,7,4,4],2))

