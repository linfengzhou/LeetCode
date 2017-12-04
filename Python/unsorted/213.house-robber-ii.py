class Solution(object):

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        rub1 = nums[1:]
        rub2 = nums[:-1]
        max1, max2 = 0, 0
        f1, f2 = [0] * len(nums), [0] * len(nums)
        f1[0], f1[1] = 0, rub1[0]
        f2[0], f2[1] = 0, rub2[0]
        for i in range(2, len(nums)):
            f1[i] = max(f1[i - 1], rub1[i - 1] + f1[i - 2])
            f2[i] = max(f2[i - 1], rub2[i - 1] + f2[i - 2])
        return max(f1[-1], f2[-1])

# if __name__ == '__main__':
#     a = Solution()
#     print(a.rob([1, 2, 3, 4, 5]))
