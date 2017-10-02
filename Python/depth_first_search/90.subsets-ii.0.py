class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res, path, start = [], [], 0
        nums.sort()
        self.dfs(path, nums, start, res)
        return res

    def dfs(self, path, nums, start, res):
        res.append(path[:])

        for i in range(start, len(nums)):
            if (i != 0 and nums[i-1] == nums[i] and i > start):
                continue
            path.append(nums[i])
            self.dfs(path, nums, i+1, res)
            path.pop()
