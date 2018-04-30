class Solution(object):

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        def dfs(x, y):
            if x < 0 or y < 0 or obstacleGrid[x][y] == 1:
                return 0
            if x == 0 and y == 0:
                return f[0][0]
            if f[x][y] > 0:
                return f[x][y]
            else:
                return f[x][y] + dfs(x - 1, y) + dfs(x, y - 1)

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        f = [[0] * n for i in range(m)]
        if obstacleGrid[0][0] == 1:
            f[0][0] = 0
        else:
            f[0][0] = 1
        return dfs(m - 1, n - 1)
