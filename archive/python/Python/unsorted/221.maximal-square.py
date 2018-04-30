class Solution(object):

    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or len(matrix[0]) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        res = 0
        f = [[0] * n for i in range(m)]
        for i in range(m):
            f[i][0] = int(matrix[i][0])
            res = max(res, f[i][0])
            for j in range(1, n):
                if i == 0:
                    f[i][j] = int(matrix[i][j])
                elif matrix[i][j] == "0":
                    f[i][j] = 0
                else:
                    f[i][j] = min(f[i - 1][j], f[i][j - 1],
                                  f[i - 1][j - 1]) + 1
                res = max(res, f[i][j])
        return res ** 2
if __name__ == '__main__':
    a = Solution()
    print(a.maximalSquare([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], [
                    "1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
