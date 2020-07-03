"""
Algo: Create a HashMap to store element-frequency pair in HashMap.
      Use a priority queue to store element-frequency pair (Max-Heap).
      Remove the top of heap K times and print the element.

T.C. - O(d + k(log d)) - O(d) time is required to traverse distinct elements
                       - O(k logd) to pop top element of the heap 'k' times, and in O(log d) time for each operation.

S.C. - O(d) - For Storing elements in HashMap O(d) space complexity is needed. It is Auxiliary space.
"""


import heapq
from collections import Counter
def topKFrequent(nums, k):
    res = []

    # Creates a dictionary with number as key and it's count in nums array as frequency by using Counter() in it
    # If d is the number of distinct elements in nums list, O(d) time is required to traverse distinct elements.
    dic = Counter(nums)

    # Making a max_heap while iterating through keys and values in it
    max_heap = []
    for key, val in dic.items():
        max_heap.append((-val,key))
    heapq.heapify(max_heap)

    # Popping of top element of heap takes O(log N) time.
    # In this case, for loop is run 'k' times, and if there are 'd' elements in dictionary, then
    # T.C. for this would be O(k log d).
    for i in range(k):
        res.append(heapq.heappop(max_heap)[1]) # Popping max_heap[1], as only the key is required for it
    return res

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))


