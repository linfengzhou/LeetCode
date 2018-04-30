# my solution
class Solution(object):

    def convert(self, s, numRows):
        if not s:
            return ""
        if numRows < 2:
            return s
        s_list = []
        total = []
        for i in range(numRows):
            s_list.append([])
        count = 0
        direct = -1
        for i, c in enumerate(s):
            s_list[count].append(c)
            if (count == 0) or (count == (numRows - 1)):
                direct = direct * -1
                count = count + direct
            else:
                count = count + direct
        for j in range(numRows):
            total = total + s_list[j]
        return ''.join(total)

# try to optimize 
# my solution  89%
class Solution(object):

    def convert(self, s, numRows):
        if not s:
            return ""
        if numRows < 2:
            return s
        total = []
        s_list = [""] * numRows
        count = 0
        direct = -1
        for i, c in enumerate(s):
            s_list[count]= s_list[count] + c
            if (count == 0) or (count == (numRows - 1)):
                direct = direct * -1
                count = count + direct
            else:
                count = count + direct
        return ''.join(s_list)
