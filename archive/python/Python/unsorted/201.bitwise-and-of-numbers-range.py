import sys


class Solution(object):

    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == n:
            return m

        r = sys.maxsize
        while (m & r) != (n & r):
            print(m & r, n & r, str(bin(r)))
            r = r << 1
        return n & r


# if __name__ == '__main__':
#     a = Solution()
#     print(a.rangeBitwiseAnd(5, 13))
