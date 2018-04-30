class Solution(object):

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s_list, t_list = [0 for i in range(256)], [0 for i in range(256)]
        for i in range(len(s)):
            if s_list[ord(s[i])] != t_list[ord(t[i])]:
                return False
            s_list[ord(s[i])] = i + 1
            t_list[ord(t[i])] = i + 1
        return True
