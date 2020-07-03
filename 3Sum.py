"""
Algo: Sort input array
      Traverse array and for every index i, create two variables 'l' = i+1 and 'r'=n-1, then until l<r and nums[i]+nums[l]+nums[r] = 0
      If the sum is less than zero then increment value of l,sum will increase as the array is sorted
      If the sum is greater than zero then decrement value of r,sum will decrease as the array is sorted

T.C. - O(N^2), 'N' number of items in nums list, as only two nested loops are there in it.
S.C - O(1) - No extra space is required in it.
"""

def threeSum(nums):
    res = []  # 'res' contains complete solution set
    nums.sort()  # sorting the numbers

    for i in range(0, len(nums) - 2):  # As 3 numbers are atleast required to continue

        if (i > 0 and nums[i] == nums[i - 1]):  #
            continue  # continue command will skip current round of for loop, which removes the duplicates

        l = i + 1
        r = len(nums) - 1

        while (l < r):
            s = nums[i] + nums[l] + nums[r]

            if (s < 0):
                l += 1  # As sum is less than 0 and 'nums' array is sorted, so incrementing l value
            elif (s > 0):
                r -= 1  # As sum is greater than 0 and 'nums' array is sorted, so decrementing r value

            else:
                res.append((nums[i], nums[l], nums[r]))  # As all unique triplets are to be found in the array

                while l < r and nums[l] == nums[l + 1]:  # In zero sum case, If there is duplicate element from 'l' side, in between then we can just increment the value of 'l'
                    l += 1
                while l < r and nums[r] == nums[r - 1]:  # In zero sum case, If there is duplicate element from 'r' side, in between then we can just decrement the value of 'r'
                    r -= 1

                # If no duplicate elements in between, just increment l and decrement r value
                l += 1
                r -= 1
    return res