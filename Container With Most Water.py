"""

Intuition : Area is there by height of shorter line, and more distant the given lines, more would be the area.
            There is no increase in area, if there is movement of longer line
            Moving the shorter line is useful, considering the relatively longer line obtained by moving the shorter line's pointer
            might overcome the reduction in area due to width reduction.
            For a better short (minimum), we are moving away from current minimum

Algorithm: Two pointers one at beginning, other at the end
            Maxarea variable to store maximum area obtained
            Every iteration, find area between them and update max area

T.C - O(N) - Iterating through all the elements of the input list
S.C - O(1) - Constant space is used
"""
import math

def maxArea(height):
    maximumArea = 0
    l = 0 # Left Pointer
    r = len(height)-1 # Right Pointer

    while(l < r):
        maximumArea = max(maximumArea, min(height[l], height[r]) * (r-l)) # Updating maximumArea when getting other maximum value

        if height[l] < height[r]: # Incrementing left pointer when height of left pointer is less than height of right pointer
            l += 1

        else:
             r -= 1

    return maximumArea

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print (maxArea(height))
