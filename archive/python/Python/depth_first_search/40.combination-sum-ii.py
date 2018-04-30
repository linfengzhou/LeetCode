class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res, path, start, visit = [], [], 0, [0]*len(candidates)
        candidates.sort()
        self.dfs(path, candidates, start, target, res, visit[:])
        return res

    def dfs(self, path, nums, start, target, res, visit):
        for i in range(start, len(nums)):
            if target < nums[i]:
                break
            if (i != 0 and nums[i-1] == nums[i] and visit[i-1] == 0):
                continue
            if target == nums[i]:
                res.append(path[:]+[nums[i]])
            path.append(nums[i])
            visit[i] = 1
            self.dfs(path, nums, i+1, target-nums[i], res, visit)
            path.pop()
            visit[i] = 0
