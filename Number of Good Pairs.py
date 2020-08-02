"""
Algo: Number of good pairs is equal to nc2, where 'n' is the frequency of each element in the nums list.
     Calculate frequency of each element, and store it in a dictionary by using Counter in Python.

T.C. - O(N) - To iterate over num_freq list to calculate goodPairCount for each element's frequency.
S.C. - O(N) - To store the frequency of elements in nums list in the dictionary.

"""

from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums):
        
        num_freq = {} # Number Frequency dictionary to maintain frequency of each number in a dictionary

        goodPairCount = 0 # Number of count of good pairs

        num_freq = Counter(nums) # Counting frequency of each number in nums list

        # using nC2 = (n*(n-1)/2) to find good pairs by iterating over the values in num_freq
        for item in num_freq.values():
            goodPairCount += ((item) * (item-1))//2
        
        return goodPairCount

nums = [1,2,3,1,1,3]

print(Solution().numIdenticalPairs(nums))