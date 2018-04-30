class Solution(object):

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            for i, c in enumerate(nums):
                if c == target:
                    return i
        else:
            for i, c in enumerate(nums):
                if nums[0] > target:
                    return 0
                elif nums[len(nums) - 1] < target:
                    return len(nums)
                else:
                    if nums[i - 1] < target and nums[i] > target:
                        return i
