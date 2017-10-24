class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if not nums or len(nums) == 0:
            return res

        nums.sort()

        for i in range(len(nums)):
            a = nums[i]
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            target = -1 * a
            j, k = i + 1, len(nums) - 1
            while j < k:
                temp_sum = nums[j] + nums[k]
                if temp_sum == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while (j < k and j != i + 1 and nums[j] == nums[j - 1]):
                        j += 1
                    while (j < k and k != len(nums) - 1 and nums[k] == nums[k + 1]):
                        k -= 1
                elif temp_sum < target:
                    j += 1
                else:
                    k -= 1
        return res
