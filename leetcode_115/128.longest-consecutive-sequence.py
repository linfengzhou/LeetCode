class Solution(object):

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in nums:
                temp = num + 1
                while temp in nums:
                    temp += 1
                res = max(res, temp - num)
        return res

if __name__ == '__main__':
    a = Solution()
    print(a.longestConsecutive([8, 7, 23, 345, 6412,
                               9, 31, 30, 29, 28, 6, 14, 15, 16, 90, 21]))
