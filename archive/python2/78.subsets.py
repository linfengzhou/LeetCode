class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res, path, start = [], [], 0
        self.dfshelper(path,nums,start,res)
        return res

    def dfshelper(self, path, nums, start, res):
        res.append(path[:])

        for i in range(start, len(nums)):
            path.append(nums[i])
            self.dfshelper(path, nums, i+1, res)
            path.pop()

