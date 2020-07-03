"""
Algo: Use concept of Dynamic Programming
    dp[i][j] = dp[i][j-1] + dp[i-1][j]
    So, dp[i][j] represents number of unique paths to reach point (i,j)

T.C. - O(M*N) time - as need to traverse through complete matrix
S.C.- O(M*N) - New matrix of size M*N is created.
"""

def uniquePaths(m, n):

    # Edge cases
    if (m<=0 or n<=0):
        return 0

    if (m==1 or n==1):
        return 1

    # Building a matrix
    matrix = [[1 for j in range(n)] for i in range(m) ]

    for i in range(1,m):
        for j in range(1,n):

            # Use concept of DP, as robot can only move down or right at any point of time
            # So, matrix[i][j] represents number of unique paths to reach point (i,j)
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

    return matrix[-1][-1]

m = 3
n = 2
print (uniquePaths(3,2))

