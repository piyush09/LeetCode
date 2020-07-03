"""
Algo: Compute difference of actual sum of 'n' numbers and given numbers
      Return the difference.
T.C. - O(n), summing of all numbers costs O(N) time, although actual sum can be computed in O(1) time
S.C. - O(1)- Constant memory usage
"""

def missingNumber(nums):
    numbersSum = sum(nums)
    n = len(nums)
    actualSum = ((n) * (n + 1)) // 2

    return (actualSum - numbersSum)

nums = [0]
print (missingNumber(nums))
