class Solution(object):

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num1 or not num2:
            return None

        len1, len2 = len(num1), len(num2)
        len3 = len1 + len2
        carry = 0
        nums = [0] * len3
        i, j = len1 - 1, len2 - 1
        for i in range(len1 - 1, -1, -1):
            num_i = int(num1[i])
            carry = 0
            for j in range(len2 - 1, -1, -1):
                num_j = int(num2[j])
                product = num_i * num_j
#                 print(i, j, num_i*num_j, carry, nums[i + j + 1])
                total = product + carry + nums[i + j + 1]
                carry = total // 10
                nums[i + j + 1] = total % 10
            nums[i + j] += carry
        total_s = ''
        for i in range(len(nums)):
            if total_s == '' and i != len(nums) - 1 and nums[i] == 0:
                continue
            total_s += str(nums[i])
        return total_s
