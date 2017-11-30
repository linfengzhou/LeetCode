from collections import deque


class Solution(object):

    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums or s == 0 or len(nums) == 0:
            return 0
        cur_sum, cur_window, cur_len = 0, deque([]), 0
        n = len(nums)
        res = None
        for i in nums:
            cur_sum += i
            cur_window.append(i)
            cur_len += 1
            while cur_sum >= s:
                if not res:
                    res = cur_len
                else:
                    res = min(res, cur_len)
                cur_sum -= cur_window.popleft()
                cur_len -= 1
        if not res:
            return 0
        return res

# if __name__ == '__main__':
#     a = Solution()
#     print(a.minSubArrayLen(15, [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]))
