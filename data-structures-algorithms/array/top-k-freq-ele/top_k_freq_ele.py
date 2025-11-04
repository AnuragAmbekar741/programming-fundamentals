def top_k_freq_ele(nums:list[int],k:int)->int or bool:
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