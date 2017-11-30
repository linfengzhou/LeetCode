import sys


class Solution(object):

    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0 or s == 0:
            return 0

        sums = []
        temp_sum = 0

        for i in nums:
            temp_sum += i
            sums.append(temp_sum)

        res = sys.maxsize
        for index, total_sum in enumerate(sums):
            target = total_sum - s
            if target >= 0:
                start = self.binary_search(sums, total_sum - s, index)
                res = min(res, index - start)
        if res == sys.maxsize:
            return 0
        else:
            return res

    def binary_search(self, nums, target, end):
        start = 0
        while start + 1 < end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid

        if nums[start] > target:
            return start
        else:
            return end

# if __name__ == '__main__':
#     a = Solution()
#     print(a.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
