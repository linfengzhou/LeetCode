class Solution(object):

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0

        n = len(nums)
        f = [0] * (n + 1)

        f[0] = 0
        f[1] = nums[0]

        for i in range(2, n + 1):
            # f[2] = max(f[1], f[0] + nums[1])
            f[i] = max(f[i - 1], f[i - 2] + nums[i - 1])

        return f[-1]
