class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        res = 0
        i = 0
        while i < len(nums):
            nums[res] = nums[i]
            res += 1
            i += 1
            while i < len(nums) and i != 0 and nums[i] == nums[i - 1]:
                i += 1
