class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev, cur = 0, 1
        for i in range(1, n + 1):
            tmp = cur
            cur += prev
            prev = tmp
        return cur
