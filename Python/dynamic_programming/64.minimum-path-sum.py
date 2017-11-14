class Solution(object):

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or len(grid) == 0:
            return -1
        if not grid[0] or len(grid[0]) == 0:
            return -1

        n = len(grid)
        m = len(grid[0])

        f = [[0] * m for i in range(n)]
        f[0][0] = grid[0][0]

        for i in range(1, m):
            f[0][i] = f[0][i - 1] + grid[0][i]

        for j in range(1, n):
            f[j][0] = f[j - 1][0] + grid[j][0]

        for i in range(1, n):
            for j in range(1, m):
                f[i][j] = grid[i][j] + min(f[i - 1][j], f[i][j - 1])

        return f[n - 1][m - 1]

# if __name__ == '__main__':
#     a = Solution()
#     print(a.minPathSum([[1,2,5],[3,2,1]]
#                        ))
