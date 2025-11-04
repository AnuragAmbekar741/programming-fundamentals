def prod_of_arr_except_self(nums:list[int])->list[int]:
    prod_of_all = 1
    result = []
    for num in nums:
        prod_of_all*= num
    
    for num in nums:
        result.append((prod_of_all//num))
    
    return result

print(prod_of_arr_except_self([1,2,3,4]))


def prod_of_arr_except_self2(nums:list[int])->list[int]:
    n = len(nums)
    result = [1]*n
    print(result)
    for i in range(1,n):
        result[i] = result[i-1]*nums[i-1]
    suffix = 1
    for i in range(n-1, -1, -1):  # Go backwards
        result[i] *= suffix       # Multiply prefix * suffix
        suffix *= nums[i]  
    return result

print(prod_of_arr_except_self2([1,2,3,4]))