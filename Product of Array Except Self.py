"""
Algo: Initialise output array corresponding to each element.
      Calculate the product of numbers to the left of each array element
      Calculate the product of numbers to right of each array element

T.C. - O(N), 'N' number of items in nums list, as two for loops to iterate through the numbers
S.C. - O(N), Output array is the only array used for it.
"""

def productExceptSelf(nums):
    output = [1] * len(nums)  # Output array values intialised to 1 with length equal to length of nums

    prod = 1  # Initialise product to 1

    for i in range(len(nums)):  # Calculating the product of numbers to the left of each array element
        output[i] = output[i] * prod
        prod = prod * nums[i]

    prod = 1  # Again making product value as 1

    for i in range(len(nums) - 1, -1, -1):  # Calculating the product of numbers to right of each array element
        output[i] = output[i] * prod
        prod = prod * nums[i]

    return output

nums = [1,2,3,4]
print (productExceptSelf(nums))