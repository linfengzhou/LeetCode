class Solution(object):

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        len_nums = len(nums)
        output = [1] * len_nums
        product = 1
        for i in range(len_nums - 1):
            product = product * nums[i]
            output[i + 1] = output[i+1] * product

        product = 1
        for i in range(len_nums - 2, -1, -1):
            product = product * nums[i + 1]
            output[i] = output[i] * product
        return output
