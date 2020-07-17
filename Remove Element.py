"""
Algo: Starting from the left every time target value is found, swap it with an item starting from the right.  

    Decrement end each time, item is the target value and only increment start if the value is ok.
    Start index reaches end index, stop after that point.

T.C. - O(N) - Iterating through the nums list once.
S.C.- O(1) - No extra space is used.
"""

class Solution:
    def removeElement(self, nums, val):
        
        # Take two pointers start and end indexes
        start = 0
        end = len(nums)-1
        
        # Iterate till start <= end index
        while start <= end:
            
            if (nums[start] == val):
                
                # Swap the start values with the end value and decrement end index
                nums[start], nums[end] = nums[end], nums[start]
                end = end -1
                
            else:
                # If no matching value, just increment start index
                start += 1

        # No of items without val, would be equal to position of start index
        return start

nums = [0,1,2,2,3,0,4,2]
val = 2

print(Solution().removeElement(nums, val))
        