class Solution(object):

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def dfs(x, y):
            if x < 0 or y < 0:
                return 0
            if x == 0 and y == 0:
                return f[0][0]
            if f[x][y] > 0:
                return f[x][y]
            else:
                return f[x][y] + dfs(x - 1, y) + dfs(x, y - 1)
        f = [[0] * n for i in range(m)]
        f[0][0] = 1

        return dfs(m - 1, n - 1)
