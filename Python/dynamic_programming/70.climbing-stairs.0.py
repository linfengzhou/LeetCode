class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n or n == 0:
            return 0
        if n < 3:
            return n
        f = [None] * (n + 1)
        f[0], f[1], f[2] = 0, 1, 2
        for i in range(3, n + 1):
            f[i] = f[i - 1] + f[i - 2]
        return f[-1]
