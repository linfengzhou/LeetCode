class Solution(object):

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 0:
            return 0
        nums = list(range(n))
        res = 0
        nums[0], nums[1] = None, None
        for i in range(1, n):
            if nums[i]:
                res += 1
                j = 2
                while i * j <= n - 1:
                    nums[i * j] = None
                    j += 1
        return res


if __name__ == '__main__':
    a = Solution()
    print(a.countPrimes(3))
