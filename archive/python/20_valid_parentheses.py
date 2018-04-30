class Solution(object):

    def isValid(self, s):
        left = "([{"
        right = ")]}"
        s_list = []
        for p in s:
            if p in left:
                s_list.append(p)
            else:
                if len(s_list) == 0:
                    return False
                else:
                    lp = s_list.pop()
                    if left.index(lp) != right.index(p):
                        return False
        if len(s_list) != 0:
            return False
        return True
