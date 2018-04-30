class Solution(object):

    def isUgly(self, num):
        if num <= 0:
            return False
        if num == 1:
            return True
        while num > 1:
            if num % 2 == 0:
                num = num / 2
            elif num % 3 == 0:
                num = num / 3
            elif num % 5 == 0:
                num = num / 5
            elif ((num % 2 != 0) and (num % 3 != 0) and (num % 5 != 0)):
                return False
        return True


class Solution(object):

    def isUgly(self, num):
        if num <= 0:
            return False
        for i in [2, 3, 5]:
            while num % i == 0:
                num = num / i
        return num == 1
