class Solution(object):

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or len(matrix[0]) == 0:
            return
        n_row = len(matrix)
        n_col = len(matrix[0])
        rows = [False] * n_row
        cols = [False] * n_col
        for i in range(n_row):
            for j in range(n_col):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True

        for i in range(n_row):
            if rows[i]:
                matrix[i] = [0] * n_col

        for j in range(n_col):
            if cols[j]:
                for i in range(n_row):
                    matrix[i][j] = 0
                    
        print(matrix)

if __name__ == '__main__':
    a = Solution()
    a.setZeroes([[0, 0, 0, 5], [4, 3, 1, 4], [
                0, 1, 1, 4], [1, 2, 1, 3], [0, 0, 1, 1]])
