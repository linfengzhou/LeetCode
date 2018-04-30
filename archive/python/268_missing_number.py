class Solution(object):

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = max(nums)
        count = 0
        for i in range(n + 1):
            count = count + i
        for j in nums:
            count = count - j
        if count == 0:
            if 0 in nums:
                return n + 1
            else:
                return 0
        return count
