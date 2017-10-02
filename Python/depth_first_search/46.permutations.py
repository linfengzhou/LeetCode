class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        path, res, visit= [], [], [0 for i in range(len(nums))]
        self.dfs(path, nums, res, visit)
        return res
    
    def dfs(self, path, nums, res, visit):
        if len(path) == len(nums):
            res.append(path[:])

        for i in range(len(nums)):
            if visit[i] == 1:
                continue
            path.append(nums[i])
            visit[i] = 1
            self.dfs(path, nums, res, visit)
            path.pop()
            visit[i] = 0 
