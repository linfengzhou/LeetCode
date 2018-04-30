class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        visit = [0] * len(nums)
        res, path, visit = [], [], visit[:] 
        self.dfs(path, nums, res, visit)
        return res

    def dfs(self, path, nums, res, visit):
        if len(path) == len(nums):
            res.append(path[:])

        for i in range(len(nums)):
            if visit[i] == 1:
                continue
            if (i != 0 and nums[i] == nums[i-1] and visit[i-1] == 0):
                continue
            path.append(nums[i])
            visit[i] = 1
            self.dfs(path, nums, res, visit)
            path.pop()
            visit[i] = 0
