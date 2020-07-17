class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # left dictionary maintains first occurence of element
        # right dictionary maintains last occurence of element
        # count dictionary maintains number of occurences of element in the input list
        left, right, count = {}, {}, {}
        for index, element in enumerate(nums):
            if element not in left: 
                left[element] = index
                # left dictionary is not updated if the element has appeared at least once in the list
            right[element] = index # right dictionary is updated as it maintains last occurence of element
            count[element] = count.get(element, 0) + 1 # At every occurence, count gets updated

        ans = len(nums)
        degree = max(count.values()) # degree contains the maximum value of all the values of count dictionary for each element
        
        for x in count: # iterating over each element in count dictionary
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1) # updating answer by the minimum of ans and new subarray

        return ans

nums = [1,2,2,3,1,4,2]
print(Solution().findShortestSubArray(nums))