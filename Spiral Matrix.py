"""
Algo: Traverse right and increment row begin.
      Traverse down and decrement col end.
      Traverse left and decrement row end.
      Traverse up and increment col begin.

      When traversing left or up, check whether the row or col still exists to prevent duplicates.

T.C. - O(N) - where N is total number of elements in the input matrix
S.C. - O(N) - Output array to store the elements
"""

def spiralOrder(matrix):
    res = []

    if len(matrix) == 0:
        return res

    rowBegin = 0
    rowEnd = len(matrix) - 1
    colBegin = 0
    colEnd = len(matrix[0]) - 1

    while (rowBegin <= rowEnd and colBegin <= colEnd):

        # Traverse Right
        for i in range(colBegin, colEnd + 1):
            res.append(matrix[rowBegin][i])

        rowBegin += 1

        # Traverse Down
        for i in range(rowBegin, rowEnd + 1):
            res.append(matrix[i][colEnd])

        colEnd -= 1

        # Traverse Left
        if (rowBegin <= rowEnd):
            # As it is moving down, and should go till colBegin
            for i in range(colEnd, colBegin-1, -1):
                res.append(matrix[rowEnd][i])

        rowEnd -= 1

        # Traverse Up
        if (colBegin <= colEnd):
            # As it is moving up and should go till rowBegin
            for i in range(rowEnd, rowBegin - 1, -1):
                res.append(matrix[i][colBegin])

        colBegin += 1

    return res


matrix =[
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ]

print (spiralOrder(matrix))

