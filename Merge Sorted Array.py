"""
Algo: Check which of the element is bigger, and correspondingly keep placing in nums1 array, and decrementing the index of that array.

Check the submitted solution with comments
"""
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # Condition is that both m and n are greater than 0
        while m > 0 and n > 0:
            # In this nums1 element is greater than nums2 element
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1 # Decreasing m value as that element has been covered/included in nums1
            else:
                # In this nums2 element is greater than nums1 element
                nums1[m+n-1] = nums2[n-1]
                n -= 1 # Decreasing n value as that element has been included in nums1
                
        # The below one is the case for those elements in nums2 which are smaller in case of the condition when m has become 0. So, initial n elements are copied from nums2 to nums1.  
        # This is the case when nums1 is [5, 6, 7, 8] and nums2 is [1, 2, 3, 4]
        if n > 0:
            nums1[:n] = nums2[:n]
            
nums1 = [1,2,3,0,0,0] 
m = 3
nums2 = [2,5,6]      
n = 3

print(Solution().merge(nums1,m,nums2,n))
print ("Sorted Array as nums1 is:")
print (nums1)