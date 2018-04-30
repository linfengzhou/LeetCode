class Solution(object):

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or len(board[0]) == 0:
            return False
        m, n = len(board), len(board[0])
        visited = [[False] * n for one in range(m)]
        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, 0, i, j, visited):
                    return True
        return False

    def dfs(self, board, word, index, i, j, visited):
        if index == len(word):
            return True

        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return False

        if visited[i][j]:
            return False

        if board[i][j] != word[index]:
            return False

        visited[i][j] = True
        condition = self.dfs(board, word, index + 1, i - 1, j, visited) or\
            self.dfs(board, word, index + 1, i + 1, j, visited) or\
            self.dfs(board, word, index + 1, i, j - 1, visited) or\
            self.dfs(board, word, index + 1, i, j + 1, visited)
        visited[i][j] = False

        return condition
