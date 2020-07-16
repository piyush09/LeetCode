"""
Algo: Use Breadth First Search (BFS) Approach.
     Start with empty set, iterate through all numbers, and add them to existing sets to create new subsets.

T.C.- O(2^N), 'N' is the number of elements in input set.
    In each step, the number of subsets doubles as each element is added to all existing subsets.
    There will be total of O(2^N) subsets.

S.C.- O(2^N), As output would have O(2^N) subsets, so space complexity is O(2^N)
"""

class Solution:
    def subsets(self, nums):
        
        subsets = []
        subsets.append([]) # Start by adding empty subset

        for currentNumber in nums: # Iterating through all the numbers in nums list

            # Take all existing subsets and insert current number in them to create new subsets
            n = len(subsets)

            for i in range(n):

                set = list(subsets[i]) # Extracting each subset at index 'i' in subset list

                set.append(currentNumber) # Appending currentNumber to each subset in the subsets list

                subsets.append(set) # Appending the new obtained set to the subsets list

        return subsets

nums = [1,2,3]

print(Solution().subsets(nums))