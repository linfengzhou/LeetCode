import sys


class Solution(object):

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()

        closed_diff = sys.maxsize
        for i in range(len(nums)):
            first = nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                left_num = nums[left]
                right_num = nums[right]
                diff = target - first - left_num - right_num
                if abs(diff) < abs(closed_diff):
                    closed_diff = diff
                if diff == 0:
                    return target
                elif diff > 0:
                    left += 1
                else:
                    right -= 1
        return target - closed_diff
