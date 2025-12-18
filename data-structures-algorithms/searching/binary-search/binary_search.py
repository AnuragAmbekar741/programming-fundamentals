import math

def binary_search(arr:list[int],target:int)->int:
    low = 0
    high = len(arr)
    while low <= high:
        mid = math.floor(low + (high-low) // 2)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid
    return -1

print(binary_search([1,2,3,4,5,6,7,8,9,10], 8))