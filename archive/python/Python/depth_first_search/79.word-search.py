class Solution(object):
    x_dir = [1, -1, 0, 0]
    y_dir = [0, 0, 1, -1]

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or len(board[0]) == 0:
            return False
        nrow, ncol = len(board), len(board[0])
        if len(word) > nrow * ncol:
            return False

        visited = [[False] * ncol for one in range(nrow)]
        for i in range(nrow):
            for j in range(ncol):
                if board[i][j] == word[0]:
                    if self.dfs(board, word, 0, i, j, visited):
                        return True
        return False

    def dfs(self, board, word, index, i, j, visited):
        if index == len(word):
            return True
        m, n = len(board), len(board[0])

        if i < 0 or j < 0 or i >= m or j >= n:
            return False
        if visited[i][j]:
            return False
        if board[i][j] != word[index]:
            return False

        res = False
        visited[i][j] = True
        for x, y in zip(self.x_dir, self.y_dir):
            res = res or self.dfs(
                board, word, index + 1, i + x, j + y, visited)
        visited[i][j] = False
        return res
