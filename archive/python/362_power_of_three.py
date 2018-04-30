class Solution(object):

    def isPowerOfThree(self, n):
        while n > 1:
            if n % 3 != 0 and n != 1:
                return False
            else:
                n = n / 3
        return True
