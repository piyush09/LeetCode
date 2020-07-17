class Solution:
    def maximalSquare(self, matrix):
        
        if not matrix:
            return 0
        
        m = len(matrix) # Number of rows of the matrix
        n = len(matrix[0]) # Number of columns of the matrix
        
        # Initializing dp matrix to 0 for 'n' columns and 'm' rows
        dp = [[0 for i in range(n)] for j in range(m)]
        
        # Maximum side length of the square in the matrix
        maxSide = 0
        
        for i in range(0, m): # Iterating it over 'm' rows of the matrix
            for j in range(0,n): # Iterating over 'n' columns of the matrix
                
                if (i == 0 or j == 0):
                    dp[i][j] = int(matrix[i][j])
                    
                elif ((int(matrix[i][j])) == 1):
                    dp[i][j] = min (dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                
                maxSide = max(maxSide, dp[i][j])
                
        return maxSide*maxSide # Returning the area of the maximum side of the possible square in the matrix

matrix = [
        [1,0, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0]
        ]
        
print(Solution().maximalSquare(matrix))