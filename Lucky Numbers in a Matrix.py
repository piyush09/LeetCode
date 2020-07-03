def luckyNumbers(matrix):
    m = len(matrix)  # m being the number of rows
    n = len(matrix[0])  # n being the number of columns

    minInRowList = []
    maxInColumnList = []

    for i in range(m):
        minInRow = min(matrix[i])
        minInRowIndex = matrix[i].index(minInRow)

        minInRowList.append((i, minInRowIndex))

    for j in range(n):
        temp = 0
        maxInColumn = matrix[0][j]
        for i in range(m):
            if (matrix[i][j] > maxInColumn):
                temp = i
                maxInColumn = matrix[i][j]

        maxInColumnRowIndex = temp
        maxInColumnList.append((maxInColumnRowIndex, j))

    luckyNumbersList = []
    indexes = []
    for item in minInRowList:
        if item in maxInColumnList:
            indexes.append(item)

    for x, y in indexes:
        luckyNumbersList.append(matrix[x][y])

    return luckyNumbersList


matrix = [
          [3,7,8],
          [9,11,13],
          [15,16,17]
         ]

print (luckyNumbers(matrix))