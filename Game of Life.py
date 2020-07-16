"""
Algo: Iterate the cells of the board.
      Change to (-1), if cell was live earlier but now dead.
      Change value to 2, if cell was dead before, but now live.
      
      Iterate board again, change value to 1, if value is greater than 0.
      Change value to 0, if value is less than or equal to 0.

T.C. - O(M*N) - M, N - dimensions of the board
S.C. - O(1) - Constant space is being used

"""

class Solution:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        
        # Neighbours array for 8 neighboring cells of a given cell
        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
        
        rows = len(board)
        cols = len(board[0])
        
        # Iterate through the board by each cell
        for row in range(rows):
            for col in range(cols):
                
                # For each cell counting number of live neighbors
                live_neighbors = 0
                for neighbor in neighbors:
                    
                    # row and column of neighboring cell
                    r = (row + neighbor[0])
                    c = (col + neighbor[1])
                    
                    # Checking validity of neighboring cell and if it was originally a live cell
                    if(r < rows and r >= 0) and (c < cols and c >= 0) and abs(board[r][c]) == 1:
                        
                        live_neighbors += 1
                
                # Rule 1 or Rule 3
                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    
                    board[row][col] = -1 # -1 meaning cell is now dead but was originally live
                
                # Rule 4
                if board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 2 #2 meaning cell is now live but was originally dead
        # Get final representation for updated board           
        for row in range(rows):
            for col in range(cols):
                
                if board[row][col] > 0:
                    board[row][col] = 1
                    
                else:
                    board[row][col] = 0

board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
        ]

print(Solution().gameOfLife(board))
print ("Next State of board is:")
print(board)