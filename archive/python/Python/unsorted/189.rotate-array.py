class Solution(object):

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or k == 0:
            return
        k = k % len(nums)
        while k > 0:
            temp = nums.pop()
            nums.insert(0, temp)
            k -= 1
