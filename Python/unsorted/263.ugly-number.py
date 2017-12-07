class Solution(object):

    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        if num == 1:
            return True
        prime, i = [2, 3, 5], 0
        while num > 1 and i < len(prime):
            res = num % prime[i]
            if res == 0:
                num = num // prime[i]
            else:
                i += 1
        if num > 1:
            return False
        else:
            return True
# if __name__ == '__main__':
#     a = Solution()
#     print(a.isUgly(16))
