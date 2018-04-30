class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        path, res, start = [], [], 1
        self.dfs(path, n+1, k, start, res)
        return res

    def dfs(self, path, n, k, start, res):
        for i in range(start, n):
            if k == 0:
                break
            if k == 1:
                res.append(path[:]+[i])
            path.append(i)
            self.dfs(path, n, k-1, i+1, res)
            path.pop()
        
