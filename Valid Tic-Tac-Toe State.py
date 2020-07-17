class Solution:
    
    def check_win_positions(self, board, player):
        
        # Checking rows (particular player is there in one complete row)
        for i in range(len(board)):
            if (board[i][0] == board[i][1] == board[i][2] == player):
                return True
        
        # Checking columns (particular player is there in one complete column)
        for i in range(len(board)):
            if (board[0][i] == board[1][i] == board[2][i] == player):
                return True
            
        
        # Checking the diagonals (particular player is in any of the 2 diagnols)
        if ((board[0][0] == board[1][1] == board[2][2] == player) or \
            (board[0][2] == board[1][1] == board[2][0] == player)):
            return True
        
        # The above are winning positions, otherwise output would be false
        return False
        
    
    def validTicTacToe(self, board):
        
        # Initializing 'x_count' and 'o_count' to 0
        x_count = 0
        o_count = 0 
        
        # Calculating 'x_count' and 'o_count' in the board
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (str(board[i][j]) == "X"):
                    x_count += 1
                    
                elif(str(board[i][j]) == "O"): # It is capital 'O' not zero
                    o_count += 1
        
        # These are the corner cases
        # As 'x' starts first, so 'x_count' should always be greater than or equal to 'o_count'
        
        # As players take turns, so it would be false if ((x_count - o_count)>1)
        if ((x_count < o_count) or ((x_count - o_count) > 1)):
            return False
        
        
        # Checking Player '0' winning
        if (self.check_win_positions(board, 'O')): # Checking if player '0' has a winning condition
            if (self.check_win_positions(board, 'X')): # Checking if player 'X' has a winning condition
                return False # It is 'False' considering that 'X' would have won earlier, and the game would have ended at that point, hence it is not possible to reach this board position
            
            if (x_count != o_count): # if 'x_count' and 'o_count' is not equal, then it is false, considering '0' always play after 'X'
                return False
            
        
        # Checking Player 'X' winning
        if (self.check_win_positions(board, 'X') and (x_count != o_count + 1)):
            return False # As player 'X' plays first move, and if player 'X' wins, then count of player 'X' would be 1 more than player '0'
        
        # If all these states are checked, then return True, considering all 'False' possible cases are checked
        return True

board = ["XOX", "O O", "XOX"]

print(Solution().validTicTacToe(board))

