def prod_of_arr_except_self(nums:list[int])->list[int]:
    prod_of_all = 1
    result = []
    for num in nums:
        prod_of_all*= num
    
    for num in nums:
        result.append((prod_of_all//num))
    
    return result

print(prod_of_arr_except_self([1,2,3,4]))