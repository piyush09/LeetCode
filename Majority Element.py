"""
Algo: Sorting approach - Sort the elements and return middle element.
T.C. - O(N log N) - Sorting the array costs O(N log N) time, and it is the major run time.
S.C. - O(1) - Constant Space.
"""
class Solution:
    def majorityElement(self, nums):
        
        nums.sort()
        return nums[len(nums)//2]

nums = [2,2,1,1,1,2,2]
print(Solution().majorityElement(nums))