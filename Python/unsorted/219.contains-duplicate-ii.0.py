class Solution(object):

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False

        dic = dict()
        for index, num in enumerate(nums):
            if num in dic and index - dic[num] <= k:
                return True
            dic[num] = index
        return False
