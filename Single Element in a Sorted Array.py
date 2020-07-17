class Solution:
    def singleNonDuplicate(self, nums):
        
        start = 0
        end = len(nums) - 1
        
        while(start < end):
            mid = start + (end - start) // 2
            
            # mid index is even
            if (mid % 2 == 0):
                
                if (nums[mid] == nums[mid+1]): # As we are considering 'eo', even odd combination, so checking if index is even, then whether next odd index is matching. 
                    start = mid + 2 # In case of match, as previous array is sorted, so changing the start value in that case
                    
                else:
                    end = mid # As there is no match (considering 'eo' (even odd index not matching), then element occuring once in sorted array is occuring before mid index
             
            # mid index is odd
            else:
                if (nums[mid] == nums[mid-1]): # if 'eo' match is occuring, then single element occurs after this element
                    start = mid + 1
                else:
                    end = mid
                    
            
        return nums[start]

nums = [3,3,7,7,10,11,11]
print(Solution().singleNonDuplicate(nums))