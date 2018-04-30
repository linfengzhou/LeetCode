class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, n_len, i = 0, len(nums), 0
        if not nums or len(nums) == 0:
            return res

        while i < n_len:
            if i != 0 and i < n_len and nums[i - 1] == nums[i]:
                while i != 0 and i < n_len and nums[i - 1] == nums[i]:
                    i += 1
            else:
                nums[res] = nums[i]
                res += 1
                i += 1
