"""
Algo: Dynamic Programming Approach used for the same.
    While iterating through 'nums' list, Keep track of maximum product upto the number (which is max_so_far)
      'max_so_far' is tracked to accumulate product of positive numbers. 
      and minimum product upto the number (min_so_far) ('min_so_far' is tracked to handle negative numbers).

      Update max_so_far by taking maximum of: 
        a) Current Number - It can be chosen, if the product already accumulated is less or when the preceding number
                            is a zero or a negative number.

        b) Product of last max_so_far and current number - This value will be picked if the accumulated product has been increasing
                         (all positive numbers)

        c) Product of last min_so_far and current number - This value will be picked if the current number is a negative number
                     and the combo chain is disrupted by a single negative number before.
                     min_so_far is updated in using the same three numbers and taking minimum among them.

T.C. - O(N) - as iterating through nums only once.
S.C. - O(1) - as no additional space is being used as variables are only being used for storing results individually.
"""

class Solution:
    def maxProduct(self, nums):
        
        if len(nums) == 0:
            return 0

        max_so_far = nums[0] 
        min_so_far = nums[0]
        result = max_so_far
        
        for i in range(1, len(nums)):
            
            curr = nums[i]
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

            max_so_far = temp_max 

            result = max(max_so_far, result)

        return result

# nums = [2,3,-2,4]
# nums = [0,2]

nums = [-3,0,1,-2]

print(Solution().maxProduct(nums))
    
        