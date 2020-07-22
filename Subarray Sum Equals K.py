"""
Algo: Whenever the sum has increased by a value of k, there exists a subarray of sums=k.
      dictionary is used to store cumulative sum upto all indices, along with number of times the same sum occurs.
      (sum(i), number of occurences of sum(i)) in this format.

      If there is a new sum, make entry in dictionary according to that sum.
      If same sum occurs again, then increment the count corresponding to that sum in the dictionary.

      Check the number of times (sum-k) has occured already, 
      as it will count the number of times a subarray with sum k has occured upto the current index. 
      Increment the count by the same number and return the count at the end of nums list.

T.C. - O(N) - entire nums array is traversed only once.
S.C. - O(N) - Hashmap/ Dictionary can contain upto n distinct entries in the worst case.
"""

class Solution:
    def subarraySum(self, nums, k):
        
        count = 0
        sums = 0
        d = dict()
        d[0] = 1 # Initialise in the dictionary with key as 0, and value as 1
        
        for i in range(len(nums)):
            sums += nums[i] # Adding each number as iterating in the nums list.
            count += d.get(sums-k,0) # Incrementing count by the number of times (sums-k) has occured in the array.
            d[sums] = d.get(sums,0) + 1

        return count

nums = [1,1,1]
k = 2

# nums = [1,2,3]
# k = 3

print(Solution().subarraySum(nums,k))

