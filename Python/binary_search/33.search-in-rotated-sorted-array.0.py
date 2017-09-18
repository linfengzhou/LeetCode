class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 2:
            if target not in nums:
                return -1
            else:
                return 0
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[start]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid
                else:
                    start = mid
            if nums[mid] < nums[start]:
                if target <= nums[end] and nums[mid] < target:
                    start = mid
                else:
                    end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        else:
            return -1
