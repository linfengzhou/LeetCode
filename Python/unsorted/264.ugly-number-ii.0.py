class Solution(object):

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1]
        p2, p3, p5 = 0, 0, 0
        for i in range(1, n):
            last = res[-1]
            while res[p2] * 2 <= last:
                p2 += 1
            while res[p3] * 3 <= last:
                p3 += 1
            while res[p5] * 5 <= last:
                p5 += 1
            new = min(2 * res[p2], 3 * res[p3], 5 * res[p5])
            res.append(new)
        return res[-1]
