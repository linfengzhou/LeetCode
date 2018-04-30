class Solution(object):

    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if nums[0] > nums[1]:
            return 0
        elif nums[n - 1] > nums[n - 2]:
            return n - 1
        else:
            for i in range(n):
                if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                    return i
