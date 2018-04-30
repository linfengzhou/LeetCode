class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        path, res, start = [], [], 0
        self.dfs(path, candidates, start, target, res)
        return res
        
    def dfs(self, path, nums, start, target, res):
        for i in range(start, len(nums)):
            if target < nums[i]:
                break
            if target == nums[i]:
                res.append(path[:]+[nums[i]])
            path.append(nums[i])
            self.dfs(path, nums, i, target-nums[i], res)
            path.pop()
