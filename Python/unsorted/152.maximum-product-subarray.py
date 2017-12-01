import sys


class Solution(object):

    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0

        max_product, min_product, res = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            temp = max_product
            num = nums[i]
            max_product = max(
                max(max_product * num, min_product * num), num)
            min_product = min(
                min(min_product * num, temp * num), num)
            if max_product > res:
                res = max_product
        return res

# if __name__ == '__main__':
#     a = Solution()
#     print(a.maxProduct([2, 3, -1]))
