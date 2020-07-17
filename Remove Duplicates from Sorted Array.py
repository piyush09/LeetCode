class Solution:
    def removeDuplicates(self, nums):
        
        if (len(nums)<2): # Checking case for which length of nums list is 0 or 1
            return len(nums)
        
        new_index = 0 # Creating a new index
        
        for i in range(1, len(nums)):  # Given array is a sorted array
            if nums[i] != nums[new_index]:
                new_index +=1
                nums[new_index] = nums[i]
        # In this problem, it doesn't matter what values are set beyond the returned length.
        
        return new_index + 1 # As we are returning length, so adding 1 to it
                             # Answer is still an array as the array is passed by reference
        
        """
        :type nums: List[int]
        :rtype: int
        """

nums = [0,0,1,1,1,2,2,3,3,4]
print (Solution().removeDuplicates(nums))