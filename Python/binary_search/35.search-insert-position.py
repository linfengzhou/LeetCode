class Solution(object):

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] == target:  # speed up
                return mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] >= target:
            return start
        elif nums[end] >= target:
            return end
        else:
            return end + 1
