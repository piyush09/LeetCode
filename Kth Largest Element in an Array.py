"""
Algo: Form a min heap for all the elements in nums list.
      Pop (n-k) elements from the heap to get kth largest element in the array.

T.C. - O(N + (N-K) log N) - O(N) for building heap, and (N-K) times operation of O(log N) for popping an element from it
S.C. - O(N) - as heap is formed for N elements in it
"""
import heapq

def findKthLargest(nums, k):
    heap = []

    # Forming a min-heap for the numbers in nums list
    for num in nums: # O(N) time complexity for building a heap
        heapq.heappush(heap, num)

    # Popping out (n-k) elements from min heap to get kth largest element in the heap and returning it
    # Time Complexity of removing an element from a heap is O(log N), because it is required to maintain
    # max/min at the root node, which takes log N operations.
    for i in range(len(nums) - k): # O(n-k) times
        heapq.heappop(heap) # O(log N)

    return heapq.heappop(heap)

nums = [3,2,1,5,6,4]
k = 2

print (findKthLargest(nums,k))