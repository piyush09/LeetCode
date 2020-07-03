"""
Algo: Make a set and iterate through the numbers list.
     Keep on adding the item to the set, if item exists in set, then there is an existence of duplicate in the numbers list.

T.C. - O(N), as search() operation and insert() operations are done 'N'(items in nums list) number of times, and each operation takes constant time.
S.C. - O(N), space is used by set, with the number of elements in it.
"""

def containsDuplicate(nums):
    numberSet = set()

    for item in nums:
        if item in numberSet:
            return True
        numberSet.add(item)

    return False

nums = [1,2,3,1]

print (containsDuplicate(nums))