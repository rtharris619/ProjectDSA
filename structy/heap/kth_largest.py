import heapq

# Write a function, kth_largest, that takes in a list of numbers and a value, k.
# The function should return the k-th largest element of the list.

def kth_largest(numbers, k):
    heap = numbers[0:k]
    heapq.heapify(heap)
    # maintaining 'k' items in the heap...
    for i in range(k, len(numbers)):
        heapq.heappush(heap, numbers[i])
        heapq.heappop(heap)
    return heapq.heappop(heap)

def kth_largest_better(numbers, k):
    heap = []
    for num in numbers:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heapq.heappop(heap)

def driver():
    res = kth_largest_better([9,2,6,6,1,5,8,7], 3) # -> 7
    print(res)
