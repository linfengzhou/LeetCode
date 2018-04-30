class Solution(object):

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res_set = set()
        for num in nums:
            res_set.add(num)

        res = 0
        for i in range(len(nums)):
            down = nums[i] - 1
            while down in res_set:
                res_set.remove(down)
                down -= 1
            up = nums[i] + 1
            while up in res_set:
                res_set.remove(up)
                up += 1

            res = max(res, up - down - 1)
        return res
