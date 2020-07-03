"""
Algo:  Maximum Product of Three Numbers could be max of these two cases:
        Product of 3 maximum numbers in the array
        Product of two minimum values and maximum value in the array

Approach 1: Sort the given nums array(in ascending order) and find out the product of the corresponding numbers. TC - O(nlogn), SC - O(logN) as sorting takes O(logN) space
        when using recursion to sort, it takes O(logN) time, when pushing elements to           stack.

Approach 2: Find the required 2 smallest values(min1 and min2) and the three largest values(max1, max2, max3) in the nums array, by iterating over thenums array only once.
Find out the product of the corresponding numbers.

        T.C. - O(N)
        S.C. - O(1) - Constant space is being used

"""

def maximumProduct(nums):
    min1 = float("inf")
    min2 = float("inf")
    max1 = float("-inf")
    max2 = float("-inf")
    max3 = float("-inf")

    for num in nums:

        if (num <= min1): # num is less than min1 and min2
            min2 = min1
            min1 = num
        elif (min1 < num <= min2): # num between min1 and min2
            min2 = num

        if (num >= max1): # num is greater than max1, max2, max3

            max3 = max2
            max2 = max1
            max1 = num

        elif (max1 > num >= max2): # num is between max1 and max2
            max3 = max2
            max2 = num

        elif (max2 > num >= max3): # num is between max2 and max3
            max3 = num
    # Returning maximum of both the possible products
    return max(min1 * min2 * max1, max1 * max2 * max3)

nums = [1,2,3]
print (maximumProduct(nums))