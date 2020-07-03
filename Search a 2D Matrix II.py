def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """

    if (matrix is None or len(matrix) < 1 or len(matrix[0]) < 1):
        return False

    row = 0
    column = len((matrix)[0]) - 1

    # Iterating till col is greater than 0 and till last row is reached
    while (column >= 0 and row <= len(matrix) - 1):

        if (target == matrix[row][column]):  # If value found, return value
            return True
        elif (target < matrix[row][column]):  # If target is less, decrement column
            column -= 1
        elif (target > matrix[row][column]):  # If target is more, increment row
            row += 1

    return False

matrix = [[-1,3]]
target = 3

print (searchMatrix(matrix, target))