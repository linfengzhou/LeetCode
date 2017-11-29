class Solution(object):
    alpha_dict = dict(
        zip(range(1, 27), list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')))

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ""
        return self.convertToTitle((n - 1) // 26) + (self.alpha_dict[(n - 1) % 26 + 1])


# if __name__ == '__main__':
#     a = Solution()
#     print(a.convertToTitle(705))
