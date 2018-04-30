class Solution(object):

    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == len(t) == 0 or abs(len(s) - len(t)) > 1:
            return False

        if len(s) < len(t):
            s, t = t, s
        # add or delete
        if abs(len(s) - len(t)) == 1:
            return self.oneedit(s, t)
        # replace
        else:
            return self.onereplace(s, t)

    def oneedit(self, s, t):
        count = 1
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            elif count == 1 and s[i] != t[j]:
                count -= 1
                i += 1
            else:
                return False
        if i == len(s) - 1 and count == 0:
            return False
        return True

    def onereplace(self, s, t):
        count = 1
        i = 0
        while i < len(s):
            if s[i] != t[i]:
                count -= 1
            if count < 0:
                return False
            i += 1
        return count == 0


# if __name__ == '__main__':
#     a = Solution()
#     print(a.isOneEditDistance('abccc', 'qabccd'))
