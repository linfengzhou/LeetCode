class Solution(object):

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        # conner case
        if (not grid) or (len(grid) == 0) or (len(grid[0]) == 0):
            return 0

        n_row = len(grid)
        n_col = len(grid[0])
        n_islands = 0

        for i in range(n_row):
            for j in range(n_col):
                if (grid[i][j]) == '1':
                    grid = self.bfs(grid, i, j)
                    n_islands += 1

        return n_islands

    def bfs(self, grid, x, y):
        def check_bound(x, y, n, m):
            if x < 0:
                return True
            if y < 0:
                return True
            if x > n - 1:
                return True
            if y > m - 1:
                return True
            return False

        directionX = [0, 1, 0, -1]
        directionY = [1, 0, -1, 0]

        queue = [[x, y]]
        grid[x][y] = '0'

        n_row = len(grid)
        n_col = len(grid[0])

        while len(queue) != 0:
            node = queue.pop()
            x, y = node[0], node[1]
            for i in range(4):
                temp_x = x + directionX[i]
                temp_y = y + directionY[i]
                if check_bound(temp_x, temp_y, n_row, n_col):
                    continue
                if grid[temp_x][temp_y] == '1':
                    grid[temp_x][temp_y] = '0'
                    queue.append([temp_x, temp_y])
        return grid
