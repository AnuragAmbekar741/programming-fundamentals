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

import heapq
from collections import Counter

def topKFrequent(nums: list[int], k: int) -> list[int]:
    freq = Counter(nums)  # O(n)

    # Build a min-heap of (frequency, num) with at most k elements
    heap: list[tuple[int, int]] = []
    for num, count in freq.items():
        if len(heap) < k:
            heapq.heappush(heap, (count, num))
        else:
            if count > heap[0][0]:
                heapq.heapreplace(heap, (count, num))

    # Extract just the numbers
    return [num for _, num in heap]
print(topKFrequent([1,22,3,4,5,3,1,3],3))