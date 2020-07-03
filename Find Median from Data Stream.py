"""
Algo: maintain two heaps
      A max-heap to store the smaller half of the input numbers
      A min-heap to store the larger half of the input numbers
      While adding the number, do not disturb the size property of the two heaps.
      Each element is added to min-heap(Large) first, then minimum element in min heap(large)
      is popped out and offered to maxHeap(small) [Assumption all elements in minHeap are greater than in maxHeap].
      Now the two heaps need to be load balanced.

T.C. - O(log N) for adding numbers, and O(1) for finding median
S.C. - O(N) - to hold the elements (numbers) in heaps
"""

from heapq import *
# heapq in Python is a min-heap.
small = [] # smaller half of list, max-heap(invert min-heap)
large = [] # Larger half of list, min-heap

# heappush(heap, ele) function is used to insert the element mentioned in its arguments into heap.
# The order is adjusted, so as heap structure is maintained.

# heappushpop(heap, ele) :- This function combines the functioning of both push and pop operations
# in one statement, increasing efficiency.
# Heap order is maintained after this operation.

def addNum(num):
    if len(small) == len(large):
        # (-num) for getting the item, as it is stored inversely
        heappush(large, -heappushpop(small,-num)) # Pushing elem in large heap
    else:
        heappush(small, -heappushpop(large, num)) # Pushing elem in small heap

def Median():

    if (len(small) == len(large)):
        # (-) sign as small is inverted minHeap.
        return float((large[0]-small[0])/2.0)
    else:
        return float(large[0])



addNum(1)
addNum(2)
print ("Median 1 is:", Median())
addNum(3)
print ("Median 2 is:",Median())