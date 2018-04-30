class Solution(object):

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        if not nums or len(nums) == 0:
            return res
        nums.sort()
        for index, first in enumerate(nums):
            if index != 0 and first == nums[index - 1]:
                continue
            for s_index in range(index + 1, len(nums)):
                if s_index != index + 1 and nums[s_index] == nums[s_index - 1]:
                    continue
                second = nums[s_index]
                left, right = s_index + 1, len(nums) - 1
                while left < right:
                    third = nums[left]
                    forth = nums[right]
                    total = first + second + third + forth
                    if target == total:
                        res.append(
                            [first, second, third, forth]
                        )
                        left += 1
                        right -= 1
                        # avoid duplicates
                        while left < right and left != 0 and \
                                nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and right != len(nums) - 1 and \
                                nums[right] == nums[right + 1]:
                            right -= 1
                    elif target > total:
                        left += 1
                    else:
                        right -= 1
        return res
