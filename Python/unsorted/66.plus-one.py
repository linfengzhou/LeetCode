class Solution(object):

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return digits

        digits[-1] += 1
        i = len(digits) - 1
        carry = 0
        while i >= 0:
            digits[i] += carry
            if digits[i] > 9:
                carry = digits[i] // 10
                digits[i] = digits[i] % 10
            else:
                carry = 0
            i -= 1
        if carry != 0:
            digits.insert(0, carry)
        return digits

# if __name__ == '__main__':
#     a = Solution()
#     print(a.plusOne([9, 9, 9]))
