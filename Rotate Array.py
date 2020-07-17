class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        k = k % n # Doing modulo operation
        
        # print (nums[(n-k):]) # Accessing last (k) elements of the array
        # print (nums[:(n-k)]) # Accessing first (n-k) elements of the array 
        
        nums[:] = nums[(n-k):] + nums[:(n-k)] # Placing last (k) elements first and then last (n-k) elements
        
        # print (nums)

nums = [1,2,3,4,5,6,7]
k = 3

Solution().rotate(nums,k)
print ("Array after rotating by K steps")
        
print(nums)