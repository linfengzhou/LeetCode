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
        f = [1, 2]
        for i in range(3, n + 1):
            # f[3] ==> f[0]  f[4] ==> f[1]
            f[(i - 1) % 2] = f[(i - 1) % 2] + f[(i - 2) % 2]
        return f[(n - 1) % 2]
