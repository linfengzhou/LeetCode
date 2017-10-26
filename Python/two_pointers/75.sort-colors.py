class Solution(object):

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums_map = {}
        for num in nums:
            nums_map.setdefault(num, 0)
            nums_map[num] += 1
        index = 0
        for num in nums_map:
            count = nums_map[num]
            while count > 0:
                nums[index] = num
                count -= 1
                index += 1
