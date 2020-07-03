"""
Algo: Iterate through all the elements of the array
      When iterating through each element of nums list, update current_sum with already curr_sum value + element value,
      or only the element's value, check which of them is maximum and update it.
      Similarly, in each iteration update the max_sum value.

T.C. - O(N), 'N' number of items in nums list, as iterating through all the numbers once.
S.C. - O(1), constant space is used.
"""

def maxSubArray(nums):
    max_sum = nums[0]  # Initializing max_sum to first element of nums list
    curr_sum = nums[0]  # Initializing curr_sum to first element of nums list

    for i in range(1, len(nums)):
        curr_sum = max(nums[i], curr_sum + nums[i])
        max_sum = max(curr_sum, max_sum)

    return max_sum  # Returning the maximum sum value

nums = [-2,1,-3,4,-1,2,1,-5,4]
print (maxSubArray(nums))