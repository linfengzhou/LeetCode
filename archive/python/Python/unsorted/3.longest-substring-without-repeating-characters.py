class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        left = 0
        last = {}
        for i in range(len(s)):
            if s[i] in last and last[s[i]] >= left:
                left = last[s[i]] + 1
            else:
                res = max(res, i - left + 1)
            last[s[i]] = i
        return res
