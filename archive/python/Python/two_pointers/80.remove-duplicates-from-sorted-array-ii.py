class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        res, temp = 0, 1
        for i in range(len(nums)):
            if nums[res] != nums[i]:
                res += 1
                nums[res] = nums[i]
                temp = 1
            elif nums[res] == nums[i] and temp < 2:
                temp += 1
                res += 1
                nums[res] = nums[i]
            else:
                temp += 1
        return res + 1
# if __name__ == '__main__':
#     a = Solution()
#     print(a.removeDuplicates([1, 1, 2, 2, 3, 3, 3, 4, 5]))
