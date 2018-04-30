class Solution(object):

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        f = [0] * n
        f[0] = 1
        for i in range(m):
            if f[0] == 0 or obstacleGrid[i][0] == 1:
                f[0] = 0
            else:
                f[0] = 1
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    f[j] = 0
                else:
                    f[j] = f[j - 1] + f[j]
        return f[n - 1]

# if __name__ == '__main__':
#     a = Solution()
#     t = a.uniquePathsWithObstacles([
#         [0, 0, 0],
#         [0, 1, 0],
#         [0, 0, 0]
#     ])
#     print(t)
