class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones, twos = 0, 0
        for num in nums:
            ones = (ones ^ i) & (~ twos)
            twos = (twos ^ i) & (~ ones)
        return ones
