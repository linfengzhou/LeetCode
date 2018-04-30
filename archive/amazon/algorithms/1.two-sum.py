class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        target_dict = dict()
        for index, num in enumerate(nums):
            if num in target_dict:
                return [target_dict[num], index]
            res = target - num
            target_dict[res] = index
        return [-1, -1]
