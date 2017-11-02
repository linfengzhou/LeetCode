class Solution(object):

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) < 2:
            return
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                break
        else:
            nums.reverse()
            return

        for j in range(len(nums) - 1, i, -1):
            if nums[j] > nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                break
        nums[i + 1:] = sorted(nums[i + 1:])
        # reverse_len = (len(nums) - 1) - i
        # for index in range(reverse_len // 2):
        #     nums[i + 1 + index], nums[len(nums) - 1 - index] = nums[
        #         len(nums) - 1 - index], nums[i + 1 + index]
