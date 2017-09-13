class Solution(object):

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        n_row = len(matrix)
        n_col = len(matrix[0])
        start, end = 0, n_row * n_col - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            mid_row = mid / n_col
            mid_col = mid % n_col
            mid_val = matrix[mid_row][mid_col]
            if mid_val == target:
                return True
            elif mid_val < target:
                start = mid
            else:
                end = mid

        if matrix[start / n_col][start % n_col] == target:
            return True
        elif matrix[end / n_col][end % n_col] == target:
            return True
        else:
            return False
