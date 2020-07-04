"""
https://www.geeksforgeeks.org/count-set-bits-in-an-integer/

Algo: Loop through all bits in an integer, check if a bit is set and if it is then increment the set bit count.

T.C. - Theta(log N).
S.C. - Space complexity is O(1), as no additional space is allocated.
"""

class Solution:
    def hammingWeight(self, n):
        # Initialising number of set bits (1 bits) to zero
        result = 0

        while (n):
            result += (n & 1)  # If a bit is set, then incrementing the result accordingly
            n >>= 1
        return result

n = 00000000000000000000000010000000
# n = 11111111111111111111111111111101

test = Solution()
print (test.hammingWeight(n))