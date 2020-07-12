"""
Algo: If 'n' is odd, then generate a particular character for 'n' number of times.
      If 'n' is even, then generate one character for (n-1) times, and other character 1 time.

S.C. - O(N) - Space required to store 'N' characters in the string.
"""

class Solution:
    def generateTheString(self, n):

        if (n % 2 != 0): # n is odd
            return ("a" * n)

        else: # 'n' is even
            return ("a" * (n - 1) + "b")


n = 5
print (Solution().generateTheString(n))