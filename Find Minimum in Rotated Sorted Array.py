"""
Algo: The main idea for our checks is to converge the left and right pointers on the start
      of the pivot, and never disqualify the index for a possible minimum value.

T.C. - O(N), 'N' number of items in nums list.
"""

def findMin(nums):

    # set left and right pointers
    left = 0
    right = len(nums) - 1

    # In this, left and right both converge to the same minimum index
    # Also, do not do left <= right, as in that, it would loop forever
    while left < right:

        # Finding middle value between left and right indexes
        mid = (left) + (right-left) // 2 # left + right would cause overflow (which would occur
        # if we are searching a massive array using a language like Java or C that has
        # fixed size integer types)

        # In this, the pivot must be occuring to the right of the middle, as that's why the values changed and became smaller
        if nums[mid] > nums[right]:
            left = mid + 1

        else:
            # In this case,the possible pivot point is at index <= mid.

            right = mid

    return nums[left]