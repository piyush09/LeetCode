class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        
        count = len(nums) # Counting and getting the length of the numbers list
        nonZeroCount = 0 # Initializing the number of non-zero numbers count as 0
        
        
        # Transferring the array, if the element is non-zero then replacing element at index 'nonZeroCount' with that element
        for i in range(0, count):
            if (nums[i] != 0): # As number is non-zero then putting/ shifting non-zero value to the left particular position
                nums [nonZeroCount] = nums[i]
                nonZeroCount += 1
            
        # Non-zero elements have been shifted to front and thus make all elements 0 from nonZeroCount to total number of elements (count)
        while nonZeroCount < count :
            nums[nonZeroCount] = 0 # Assigning all the rest positions values as 0
            nonZeroCount += 1

nums = [0,1,0,3,12]

Solution().moveZeroes(nums)
print("Moving Zeroes to the end")
print(nums)
