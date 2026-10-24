# Write a function that takes in a list of numbers and a value, k.
# The function should return the k smallest numbers in the list.
# The resulting list should be ordered from least to greatest.

import heapq

def k_smallest(nums, k):
    max_heap = []
    for num in nums:
        heapq.heappush(max_heap, (-num, num))
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    res = []
    while len(max_heap) > 0:
        ele = heapq.heappop(max_heap)[1]
        res.append(ele)
    res.reverse()
    return res

def driver():
    res = k_smallest([8, 2, 7, -3, 5, 10], 3) # -> [-3, 2, 5]
    print(res)

    res = k_smallest([84, 22, 52, 69, 71, 22, 88, 100, 13, 89, 79], 4) # -> [13, 22, 22, 52]
    print(res)
