class Solution(object):

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip().split()
        s.reverse()
        return ' '.join(s)
