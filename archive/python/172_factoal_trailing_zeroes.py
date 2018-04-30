class Solution(object):

    def trailingZeroes(self, n):
        count = 0
        product = 5
        check = n / product
        while check > 0:
            count += check
            product = product * 5
            check = n / product
        return count
