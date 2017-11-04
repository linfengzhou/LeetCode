class Solution(object):

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        max_index = 0
        for index, num in enumerate(nums):
            if max_index < index:
                return False
            current = index + num
            if current > max_index:
                max_index = current
        return True
