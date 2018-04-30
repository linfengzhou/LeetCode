class Solution(object):

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        f = [[0] * n for i in range(m)]

        for i in range(m):
            if obstacleGrid[i][0] != 1:
                f[i][0] = 1
            else:
                # f[i][0] = 0
                # cannot up
                break

        for j in range(n):
            if obstacleGrid[0][j] != 1:
                f[0][j] = 1
            else:
                # f[0][j] = 0
                # cannot left
                break

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    f[i][j] = f[i - 1][j] + f[i][j - 1]
                else:
                    f[i][j] = 0

        return f[m - 1][n - 1]

# if __name__ == '__main__':
#     a = Solution()
#     t = a.uniquePathsWithObstacles([
#         [0, 0, 0],
#         [0, 1, 0],
#         [0, 0, 0]
#     ])
#     print(t)
