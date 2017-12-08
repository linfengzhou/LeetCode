class Solution(object):

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1]
        p2, p3, p5 = 0, 0, 0
        for i in range(1, n):
            n2, n3, n5 = 2 * res[p2], 3 * res[p3], 5 * res[p5]
            new_last = min(n2, n3, n5)
            if new_last == n2:
                p2 += 1
            if new_last == n3:
                p3 += 1
            if new_last == n5:
                p5 += 1
            res.append(new_last)
        return res[-1]
