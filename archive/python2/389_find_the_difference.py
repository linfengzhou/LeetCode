class Solution(object):

    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_dict = {}
        for char in s:
            if char not in s_dict:
                s_dict[char] = 1
            else:
                s_dict[char] += 1
        for char in t:
            if char in s:
                if s_dict[char] == 0:
                    return char
                else:
                    s_dict[char] -= 1
            else:
                return char
