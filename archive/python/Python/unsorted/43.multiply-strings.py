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
        nums = [0] * len3
        for i in range(len1 - 1, -1, -1):
            num_i = int(num1[i])
            carry = 0
            for j in range(len2 - 1, -1, -1):
                num_j = int(num2[j])
                product = num_i * num_j
                total = product + nums[i + j + 1] + carry
                carry = total // 10
                nums[i + j + 1] = total % 10
            nums[i + j] += carry
        total_s = ''
        index = 0
        while index < len(nums):
            if index == 0 and nums[index] == 0:
                while index < len(nums) - 1 and nums[index] == 0:
                    index += 1
            if index < len(nums):
                total_s += str(nums[index])
                index += 1
        return total_s
