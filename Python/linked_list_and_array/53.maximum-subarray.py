import sys
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
        	return 0
        max_sum = -sys.maxsize
        total_sum = 0
        min_sum = 0
        for i in range(len(nums)):
        	total_sum += nums[i]
        	max_sum = max(max_sum, total_sum-min_sum)
        	min_sum = min(min_sum, total_sum)
        return max_sum