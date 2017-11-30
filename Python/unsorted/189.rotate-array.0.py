class Solution(object):

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or k == 0:
            return
        n = len(nums)
        k = k % n
        start_index = n - k
        temp = nums[start_index:]
        nums[k:] = nums[:start_index]
        nums[:k] = temp
