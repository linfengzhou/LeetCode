class Solution(object):

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        for i in range(len(nums)):
            if i != 0:
                res[i] = res[i - 1] * nums[i - 1]
        temp = 1
        for j in range(len(nums) - 1, -1, -1):
            if j != len(nums) - 1:
                temp = temp * nums[j + 1]
                res[j] = res[j] * temp

        return res

# if __name__ == '__main__':
#     a = Solution()
#     print(a.productExceptSelf([1, 2, 3, 4]))
