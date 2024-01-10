#the approach is by setting first row and first column corresponding to any element 0 in the matrix as 0.
#Since the element at location [0][0] of the matrix can correspond to both first row and column, an additional single storage used to flag the value of first column.
#Finally after traversing all the elements, then we check each of the flags corresponding to rows and columns and set the corresponding rows and columns as 0
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        rowZero = False

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]==0:
                    matrix[0][c]=0
                    if r>0:
                        matrix[r][0]=0
                    else:
                        rowZero = True

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c]==0 or matrix[r][0]==0:
                    matrix[r][c]=0

        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0]=0

        if rowZero:
            for c in range(cols):
                matrix[0][c]=0
