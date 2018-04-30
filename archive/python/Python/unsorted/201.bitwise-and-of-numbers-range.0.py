class Solution(object):

    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if n == m:
            return m
        if n - m == 1:
            return n & m
        else:
            return self.rangeBitwiseAnd(m >> 1, n >> 1) << 1
