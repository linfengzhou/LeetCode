class Solution(object):

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or len(matrix[0]) == 0:
            return

        n_rows = len(matrix)
        n_cols = len(matrix[0])
        first_row_zero = False
        first_col_zero = False

        for i in range(n_rows):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        for j in range(n_cols):
            if matrix[0][j] == 0:
                first_row_zero = True
                break

        for i in range(1, n_rows):
            for j in range(1, n_cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, n_rows):
            for j in range(1, n_cols):
                if (matrix[i][0] == 0) or (matrix[0][j] == 0):
                    matrix[i][j] = 0

        if first_row_zero:
            for j in range(n_cols):
                matrix[0][j] = 0

        if first_col_zero:
            for i in range(n_rows):
                matrix[i][0] = 0

#         print(matrix)

# if __name__ == '__main__':
#     a = Solution()
#     a.setZeroes([[0, 0, 0, 5], [4, 3, 1, 4], [
#                 0, 1, 1, 4], [1, 2, 1, 3], [0, 0, 1, 1]])
