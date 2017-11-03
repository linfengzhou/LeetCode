class Solution(object):

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            res = self.helper(x, -n)
            return 1.0 / res
        else:
            res = self.helper(x, n)
            return res

    def helper(self, x, n):
        if n == 0:
            return 1
        res = self.helper(x, n // 2)
        if n % 2 == 0:
            return res * res
        else:
            return res * res * x 