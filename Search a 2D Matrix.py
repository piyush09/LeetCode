def searchMatrix(matrix, target):

    if not matrix:
        return False

    m = len(matrix)
    n = len(matrix[0])
    start = matrix[0][n - 1]

    row = 0
    column = n - 1
    while (0 <= row <= m-1 and 0 <= column <= n-1):
        start = matrix[row][column]

        if (target == start):
            return True

        if (target > start):
            row += 1
            # start = matrix[row][column]

        elif (target < start):
            column -= 1


    return False

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
        ]

# target = 3
target = 25

print (searchMatrix(matrix, target))