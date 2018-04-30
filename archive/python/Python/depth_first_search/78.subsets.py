class Solution(object):

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == []:
            return nums

        result, path, start = [], [], 0
        self.dfs(path, nums, start, result)
        return result

    def dfs(self, path, nums, start, res):
        res.append(path[:])

        for i in range(start, len(nums)):
            path.append(nums[i])
            self.dfs(path, nums, i + 1, res)
            path.pop()

