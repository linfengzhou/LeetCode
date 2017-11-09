class Solution(object):

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = list(a)
        b = list(b)
        i_a, i_b = len(a) - 1, len(b) - 1
        res = []
        while i_a >= 0 and i_b >= 0:
            total = int(a[i_a]) + int(b[i_b])
            res.insert(0, total)
            i_a -= 1
            i_b -= 1

        if i_b + 1 > 0:
            res = b[:i_b + 1] + res
        else:
            res = a[:i_a + 1] + res
        # print(res)
        index = len(res) - 1
        carry = 0
        while index >= 0:
            curr = int(res[index]) + carry
            res[index] = curr % 2
            carry = curr // 2
            index -= 1
        if carry > 0:
            res.insert(0, carry)
        return ''.join([str(s) for s in res])


# if __name__ == '__main__':
#     a = Solution()
#     print(a.addBinary('1010', '1011'))
