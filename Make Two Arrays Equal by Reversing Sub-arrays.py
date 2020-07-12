"""
Algo: Make a counter of both the arrays - target and arr.
      Counter will create a hash table of an iterable.
      If both counters are equal, then true otherwise False.

T.C. - O(N)
"""

from collections import Counter
class Solution:
    def canBeEqual(self, target, arr):

        arrDict = Counter(arr)
        targetDict = Counter(target)

        if (arrDict != targetDict): # If counters are not equal, return False
            return False
        else: # If counters are equal, return True
            return True

target = [1,2,3,4]
arr = [2,4,1,3]
print (Solution().canBeEqual(target, arr))
