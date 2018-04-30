class Solution(object):

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # zero_count = 0
        left, right = 0, len(nums) - 1
        while left < right:
            # find the first left is not 0
            while left < right and nums[left] == 0:
                left += 1
            # find the first right is 0
            while left < right and nums[right] != 0:
                right -= 1

            if left < right:
                nums[left], nums[right] = nums[right], nums[left]

        right = len(nums) - 1
        while left < right:
            # find the first left is not 1
            # find the first right is 1
            # swap
            while left < right and nums[left] == 1:
                left += 1
            while left < right and nums[right] != 1:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
