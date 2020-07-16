"""
Algo: Transpose the matrix.
      Reverse each row of the matrix.

"""

class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix[0]) # n is the length of the matrix which is length of first element
        
        # Transposing the matrix
        for i in range(n):
            for j in range(i, n):
                
                # Swapping matrix[i][j] values
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
                
        # Reversing each row of the matrix
        for i in range(n):
            matrix[i].reverse()
            
        # This is in-place modification of the matrix
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]   
        ]

print(Solution().rotate(matrix))
print("Matrix After rotation (90 degrees clockwise) is:")

print(matrix)