class Solution(object):

    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_n = 0
        cur_n = 0
        for num in nums:
            if num == 0:
                max_n = max(max_n, cur_n)
                cur_n = 0
            else:
                cur_n += 1
        return max(max_n, cur_n)
