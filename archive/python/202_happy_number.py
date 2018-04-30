class Solution(object):

    def isHappy(self, n):
        n_list = list(str(n))
        unique = []
        count = 0
        while True:
            for item in n_list:
                count = count + int(item) ** 2
            if count == 1:
                return True
                break
            elif count in unique:
                return False
                break
            unique.append(count)
            n_list = list(str(count))
            count = 0
