"""
Algo: As the first house and the last house can not be both robbed, so rob(nums) = max(rob(nums[1:], nums[:-1])
    As there are no circles in both nums[1:] and nums[:-1], use answers from House Robber problem

    This approach is a DP approach for House Robber
    Using this recursive formula
    f(k) = max( f(k-2) + nums[k], f(k-1) )

T.C. - O(n) - Iterating through all numbers in nums list
S.C. - O(n) - In DP approach, making a DP array of len(nums) in order to store the max values at every index
"""

"""
    # Approach 2 for general rob (same as House Robber)
    :- Constant space use two variables and compute the max respectively
    prev = curr = 0
    for num in nums:
      temp = prev # This represents the nums[i-2]th value
      prev = curr # This represents the nums[i-1]th value
      curr = max(num + temp, prev) # just put into the formula
    return curr

This approach takes O(1) space complexity.
"""

def rob(nums):

    if not nums:
        return 0

    elif (len(nums) == 1):
        return nums[0]

    # dp[i] contains maximum amount of money stashed till ith index
    dp = [0] * len(nums)

    dp[0] = nums[0] # Initializing nums[0] value to dp[0]
    dp[1] = max(nums[0], nums[1]) # Putting dp[1] value as maximum out of nums[0] and nums[1]

    # Iterating through indexes ranging from [2,n] and updating dp values correspondingly
    for i in range(2, len(nums)):
        dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

    # Returns last element of dp table (As it is list of non negative integers, so contains maximum money)
    return dp[-1]

def advancedRob(nums):
    if not nums:
        return 0

    elif (len(nums) == 1):
        return nums[0]

    else:
        return max(rob(nums[1:]), rob(nums[:-1]))

nums = [2,3,2]
# nums = [0,0]
print (advancedRob(nums))



