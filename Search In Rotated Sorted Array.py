"""
Algorithm: Find pivot point, divide the array in two sub-arrays and call binary search.

        The ides of finding pivot element is for a sorted (in increasing order) and pivoted array,
        pivot element is the only element for which next element is smaller than it.

        Using this idea and binary search, pivot element can be found in O(log N) time.

        T.C - O(log N) - 'N' number of elements in the input list
"""

def search(nums, target):


    # Method to find rotate_index (index of smallest element in the array)
    def find_rotate_index(left, right):

        if (nums[left] < nums[right]):
            return 0 # In this case, it would be completely sorted array, and then smallest element would be 0th element

        while (left <= right):
            pivot = (left + right) // 2 # Using floored division in it

            if nums[pivot] > nums[pivot + 1]:
                return (pivot + 1) # As in that case, element at index (pivot + 1) would be smallest

            else:
                if nums[pivot] < nums[left]:
                    right = pivot - 1  # Updating the right index
                else:
                    left = pivot + 1 # Updating the left index

    # Method for standard binary_search code
    def binary_search(left, right):

        while (left <= right):

            pivot = (left + right) // 2

            if (nums[pivot] == target): # Returning the index at which element is found
                return pivot

            else:
                if (target < nums[pivot]):
                    right = pivot - 1 # Updating the right index
                else:
                    left = pivot + 1 # Updating the left index

        return -1 # In case element is not found


    # Main Function code
    n = len (nums)
    if (n == 0):
        return (-1)

    if (n == 1):
        if (nums[0] == target):
            return 0
        else:
            return (-1)

    rotate_index = find_rotate_index(0, n- 1)

    # If target is the smallest element
    if (nums[rotate_index] == target):
        return rotate_index

    # If array is not rotated, and all elements are in ascending order, binary search entire array
    if (rotate_index == 0):
        return binary_search(0, n - 1)

    if (target < nums[0]):
        # binary_search on the right side
        return binary_search(rotate_index, n - 1)

    # binary_search on the left side
    return binary_search(0, rotate_index)

nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

print (search(nums, target))