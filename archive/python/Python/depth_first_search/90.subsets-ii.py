class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res, path, start = [],[],0
        visit = [0 for i in range(len(nums))]
        nums.sort()
        self.dfs(path, nums, start, res, visit)
        return res
    
    def dfs(self, path, nums, start, res, visit):
        res.append(path[:])
        for i in range(start, len(nums)):
            if (i != 0 and nums[i] == nums[i-1] and visit[i-1] == 0):
                continue
            path.append(nums[i])
            visit[i] = 1
            self.dfs(path, nums, i+1, res, visit)
            visit[i] = 0
            path.pop()
