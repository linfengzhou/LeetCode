class Solution(object):

    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_len, t_len = len(s), len(t)
        if s_len < t_len:
            return self.isOneEditDistance(t, s)
        i = 0
        while i < len(t):
            if s[i] != t[i]:
                if s_len != t_len:
                    return s[i + 1:] == t[i:]
                else:
                    return s[i + 1:] == t[i + 1:]
            i += 1
        return s_len - t_len == 1

# if __name__ == '__main__':
#     a = Solution()
#     print(a.isOneEditDistance('a', ''))
