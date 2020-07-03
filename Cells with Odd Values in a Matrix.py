def oddCells(n, m, indices):
    matrix = [[0 for i in range(m)] for j in range(n)]

    for i in range(len(indices)):

        rowIncrement = indices[i][0]
        columnIncrement = indices[i][1]

        for p in range(m):
            matrix[rowIncrement][p] += 1

        for q in range(n):
            matrix[q][columnIncrement] += 1

    oddCount = 0

    for i in range(n):
        for j in range(m):
            if ((matrix[i][j] % 2) != 0):
                oddCount += 1

    return oddCount

# n = 2
# m = 3
# indices = [[0,1],[1,1]]

n = 2
m = 2
indices = [[1,1],[0,0]]

print (oddCells(n,m,indices))
