class Solution(object):

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or len(matrix[0]) == 0:
            return

        n_row = len(matrix)
        n_col = len(matrix[0])

        for row in range(n_row):
            for col in range(n_col):
                if row < col:
                    matrix[row][col], matrix[col][row] \
                        = matrix[col][row], matrix[row][col]
        mid = n_col // 2
        for row in range(n_row):
            for col in range(n_col):
                if n_row & 1:
                    if col >= mid:
                        continue
                    matrix[row][col], matrix[row][n_col - 1 - col]\
                        = matrix[row][n_col - 1 - col], matrix[row][col]
                elif col > mid - 1:
                    continue
                else:
                    matrix[row][col], matrix[row][n_col - 1 - col]\
                        = matrix[row][n_col - 1 - col], matrix[row][col]
