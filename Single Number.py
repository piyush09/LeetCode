"""
Algo: XOR of all array elements gives us the number with a single occurrence.
      The idea is based on the following two facts.
a) XOR of a number with itself is 0.
b) XOR of a number with 0 is number itself.

T.C. - O(N) - as iterating through every number in the nums array.
S.C. - O(1)
"""
class Solution:
    def singleNumber(self, nums):
        b = 0  # Initialising 'b' as zero, because XOR of any number with 0, is the number itself.

        for elem in nums:
            b = b ^ elem  # Doing XOR of every element in nums list

        return b

nums = [4,1,2,1,2]

print (Solution().singleNumber(nums))