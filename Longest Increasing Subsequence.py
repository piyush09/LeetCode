"""
Algo: Longest increasing subsequence possible upto the ith index in a given array
      is independent of the elements coming later on in the array

     dp[i] or temp[i] - represents the length of the longest increasing subsequence possible considering the array elements
                        upto ith index

    Check the logic in the code in order to understand algo properly.

T.C. - O(N^2) - Two 'for' loops of n are there
S.C. - O(N) - dp array (Temp) of size n is used.
"""

class Solution:
    def lengthOfLIS(self, nums):
        # Base Case
        if (len(nums) <= 1):
            return len(nums)

        # Initialising Temp array (to track longest sequence length) and filling all elements with 1 in it
        temp = [1] * len(nums)

        # One pointer is marked as i, and for each i, 'j' starts from 0
        for i in range(1, len(nums)):
            for j in range(0, i):  # 'j' will go from 0 to i

                if (nums[j] < nums[i]):  # if nums value is less, so it indicates increasing subsequence
                    temp[i] = max(temp[i], temp[j] + 1)  # Increase the value of temp[i] only if it results in larger value of the sequence

        # Return the maximum value in the 'temp' created array
        return max(temp)

s = Solution()
nums = [10,9,2,5,3,7,101,18]
print (s.lengthOfLIS(nums))