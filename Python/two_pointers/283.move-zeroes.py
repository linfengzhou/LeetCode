class Solution(object):

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left, right = 0, 1
        while left < len(nums) and right < len(nums):
            while left < len(nums) - 1 and nums[left] != 0:
                left += 1

            right = left + 1
            while right < len(nums) - 1 and nums[right] == 0:
                right += 1

            if left < len(nums) and right < len(nums):
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left += 1
                right += 1
