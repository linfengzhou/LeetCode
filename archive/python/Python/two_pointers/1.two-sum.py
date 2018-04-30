class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        n_len = len(nums) == 0
        if not nums or n_len:
            return res
        target_map = dict()
        for i, num in enumerate(nums):
            if num in target_map:
                j = target_map.get(num)
                return [min(i, j), max(i, j)]
            target_map.setdefault(target - num, i)
