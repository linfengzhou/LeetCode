class Solution(object):

    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums or s == 0 or len(nums) == 0:
            return 0
        cur_sum = 0
        cur_window = []
        n = len(nums)
        res = None
        for i in range(n):
            cur_sum += nums[i]
            cur_window.append(nums[i])
            while cur_sum >= s:
                if not res:
                    res = len(cur_window)
                else:
                    res = min(res, len(cur_window))
                cur_sum -= cur_window[0]
                cur_window.pop(0)
        if not res:
            return 0
        return res

# if __name__ == '__main__':
#     a = Solution()
#     print(a.minSubArrayLen(15, [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]))
