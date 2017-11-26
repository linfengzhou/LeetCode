class Solution(object):

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        neg = (divisor < 0) is (dividend > 0)
        ans = 0
        # each time make divisor * 2
        a, b = abs(dividend), abs(divisor)
        while a >= b:
            temp, i = b, 1
            while a >= temp:
                a -= temp
                ans += i
                temp <<= 1
                i <<= 1
        if neg:
            ans = -ans
        return min(max(-2147483648, ans), 2147483647)
