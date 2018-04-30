class Solution(object):

    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        while n > 1:
            if n % 2 != 0 and n != 1:
                return False
            else:
                n = n / 2
        return True


# def isPowerOfTwo(self, n):
#     if n <= 0:
#     	return False

#     if n & (n-1) == 0:
#     	return True

#     return False
#
