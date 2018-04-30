# my solution O(n)
class Solution(object):

    def plusOne(self, digits):
        str_list = ''
        for char in digits:
            str_list += str(char)
        int_list = int(str_list) + 1
        if int_list < 10:
            return [int_list]
        else:
            temp = []
            i = 0
            for char in str(int_list):
                temp.append(int(char))
                i = i + 1
            return temp

# normal
# [1,9,9 ] ===> [1,0,0] ==> return [2,0,0]
# [9,9] =====> [0,0] ==> [1,0,0] ==> return


class Solution(object):

    def plusOne(self, digits):
        digits.reverse()
        for index in range(len(digits)):
            if digits[index] < 9:
                digits[index] += 1
                digits.reverse()
                return digits
            else:
                digits[index] = 0

        digits.reverse()
        digits = [1] + digits
        return digits

# Good solution


class Solution(object):

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return digits

        length = len(digits) - 1
        while length >= 0:
            if digits[length] < 9:
                digits[length] += 1
                return digits
            else:
                digits[length] = 0

            length -= 1

        digits = [1] + digits
        return digits
