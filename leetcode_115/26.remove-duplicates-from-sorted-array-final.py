class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        res = 0
        for i in range(len(nums)):
            if nums[res] != nums[i]:
                res += 1
                nums[res] = nums[i]
        return res + 1
