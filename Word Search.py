"""
Algo: Start from a character and then check in each of the four direction to find a possible match.
"""

# Check whether can find word, start at i,j position
def dfs(board, i, j, word):

    # all the characters are checked
    if (len(word) == 0):
        return True

    if i<0 or i >= len(board) or j <0 or j>= len(board[0]) or word[0] != board[i][j]:
        return False

    # First character is there, check the remaining part of the word
    tmp = board[i][j]

    # Marking it as '#' in order to avoid visiting it again
    board[i][j] = '#'

    # Checking whether word can be found along one direction
    res = dfs(board, i+1, j, word[1:]) or dfs(board, i-1, j, word[1:]) \
          or dfs(board, i, j+1, word[1:]) or dfs(board, i, j-1, word[1:])

    board[i][j] = tmp
    return res


def exist(board, word):
    if not board:
        return False

    # Checking by doing dfs search on it, by passing parameters such as board, i, j and the word
    for i in range(len(board)):
        for j in range(len(board[0])):

            if dfs(board, i, j, word):
                return True

    return False

board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = "ABCCED"

print (exist(board, word))