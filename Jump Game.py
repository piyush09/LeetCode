"""
Algo: Iterating through all the indexes in the nums list.
      At every index while iterating, update the max_reach value, which indicates,
      the maximum index value, that can be reached from it.

      If the maximum reach value is greater than the last index, then it means last index is reachable.

T.C. - O(n) - single pass through the nums array, hence 'n' steps
S.C. - O(1) - Not using any extra memory
"""

def canJump(nums):

    max_reach = 0
    for i in range(0,len(nums)):

        # At every 'i' iteration, we are updating maxreach by i+nums[i] or prev. max_reach, then
        # if at any index i, (max_reach < i), then there is no way to reach that index
        if (max_reach < i):
            return  False

        # If max_reach value is greater than or equal to the end index value, then it is possible to reach end index
        if (max_reach >= len(nums)-1):
            return True

        # Updating max_reach value everytime by taking maximum of current max_reach and (i+nums[i])
        max_reach = max(max_reach, i + nums[i])

# nums = [2,3,1,1,4]
# nums = [3,2,1,0,4]
nums = [9,4,2,1,0,2,0]

print (canJump(nums))