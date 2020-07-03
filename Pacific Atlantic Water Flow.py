"""
Algo: DFS solution, Starting from each point, and dfs its neighbor if the neighbor is equal        or less than itself.
        Maintain two boolean matrix for two oceans, indicating an ocean can         reach to        that point or not.
    Go through all nodes again and see if it can be both reached by two oceans

"""

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(matrix, i, j, visited, m, n):

    # Mark that node as visited node
    visited[i][j] = True

    for dir in directions:
        x = i + dir[0]
        y = j + dir[1]

        # Can go in 4 directions with height equal or lower
        if (x < 0 or x >= m or y<0 or y >= n or visited[x][y] or matrix[i][j] > matrix[x][y] ):
            continue

        dfs(matrix, x, y, visited, m, n)

def pacificAtlantic(matrix):

    if not matrix:
        return []

    m = len(matrix) # Number of rows
    n = len(matrix[0]) # Number of columns

    # Initializing boolean matrices of pacificVisited and atlanticVisited as False for 'm' rows and 'n' columns
    # Considering marking that both pacificVisited and atlanticVisited is False for each matrix coordinate

    pacificVisited = [[False for _ in range(n)] for _ in range(m)]
    atlanticVisited = [[False for _ in range(n)] for _ in range(m)]

    # atlanticVisited = [n * [False]] * m
    result = []

    for i in range(m):
        dfs(matrix, i, 0, pacificVisited, m, n)
        dfs(matrix, i, n-1, atlanticVisited, m, n)

    for j in range(n):
        dfs(matrix, 0, j, pacificVisited, m, n)
        dfs(matrix, m-1, j, atlanticVisited, m, n)

    # Checking if both pacificVisited[i][j] and atlanticVisited[i][j] is True, then append that coordinate into the result set
    for i in range(m):
        for j in range(n):
            if (pacificVisited[i][j] and atlanticVisited[i][j]):
                result.append([i,j])

    return result


matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5], [5,1,1,2,4]]

print (pacificAtlantic(matrix))


# m =5
# n =5
# atlanticVisited = [[False for _ in range(n)] for _ in range(m)]
#
# pacificVisited = [n * [False]] * m
#
# print ("Atlantic Visited is :", atlanticVisited)
#
# print ("Pacific Visited is:", pacificVisited)