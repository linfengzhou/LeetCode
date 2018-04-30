class Solution(object):

    def createNewNum(self, num):
        n = list(str(num))
        last_number = n[0]
        count = 0
        new_number = ''
        for i in range(len(n)):
            if last_number != n[i]:
                new_number = new_number + str(count) + last_number
                count = 1
            else:
                count += 1
            last_number = n[i]
        new_number += str(count) + last_number
        return new_number

    def countAndSay(self, n):
        a = Solution()
        new_num = '1'
        for i in range(n - 1):
            if i == 0:
                new_num = a.createNewNum(1)
            else:
                new_num = a.createNewNum(int(new_num))
        return new_num
