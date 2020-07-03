"""
Algo:

T.C. - O(N), 'N' number of items in nums list.
"""

def twoSum(nums, target):
    number_dict = {}
    for index, item in enumerate(nums):

        if (target - item) in number_dict:
            return index, number_dict[target - item]
        number_dict[item] = index

    return -1, -1

nums = [2, 7, 11, 15]
target = 9
print (twoSum(nums, target))