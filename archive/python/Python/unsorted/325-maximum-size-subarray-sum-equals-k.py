class Solution(object):

    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        acc, res = 0, 0
        sum_dict = {0: -1}
        for index, num in enumerate(nums):
            acc = acc + num
            if acc not in sum_dict:
                sum_dict[acc] = index
            if acc - k in sum_dict:
                res = max(res, index - sum_dict[acc - k])
        return res
