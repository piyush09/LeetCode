"""
Algo: 
    Problem is similar to Fibonacci Number problem.
    Calculate a list of square numbers (i.e. square_nums) that is less than the given number n.

    dp[n] indicates that the perfect squares count of the given 'n' value

    Loop from the number 1 to n, to calculate the solution for each number i (i.e. numSquares(i)). 
    At each iteration, keep the result of numSquares(i) in dp[i], while reusing the previous results stored in the array.

    At the end of the loop, return the last element in the array as the result of the solution.

T.C. - O(N * (N)**1/2) - In main step, there is a nested loop, where the outer loop is of 'N' iterations 
                        and in the inner loop it takes at maximum (sqrt(N)) iterations.

S.C. - O(N) - All the intermediate sub-solutions in the array dp[].
"""
import math

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        square_nums = []
        # Calculating list of square numbers in it.
        for i in range(0, int(math.sqrt(n)+1)):
            square_nums.append(i**2)
        
        dp = [float('inf')] * (n+1) # Initially marking all values in the dp array with value as 'inf'- infinity
        # bottom case
        dp[0] = 0 # Marking value of 0th element as 0
        
        for i in range(1, n+1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i-square] + 1)
        
        return dp[-1] # Returning the last element in the dp array.

n = 13
print(Solution().numSquares(n))