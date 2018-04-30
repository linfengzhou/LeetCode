class Solution(object):

    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s1 = 0
        s2 = 0

        for c in s:
            s1 += ord(c)

        for c in t:
            s2 += ord(c)

        return chr(s2 - s1)
