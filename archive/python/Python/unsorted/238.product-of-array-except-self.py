class Solution(object):

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        res = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
                continue
            res *= num
        if zero_count > 1:
            return [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = res
            elif zero_count > 0:
                nums[i] = 0
            else:
                nums[i] = res // nums[i]
        return nums
