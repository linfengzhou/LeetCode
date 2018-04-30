class Solution(object):

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n_dict = set()
        while n not in n_dict:
            n_dict.add(n)
            temp_sum = 0
            while n > 0:
                temp_sum += (n % 10) ** 2
                n = n // 10
            n = temp_sum
            if n == 1:
                return True
        return False

# if __name__ == '__main__':
#     a = Solution()
#     print(a.isHappy(7))
