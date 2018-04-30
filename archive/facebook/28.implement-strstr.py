class Solution(object):

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if (not haystack and not needle) or needle == haystack:
            return 0
        sub_len = len(needle)
        for i in range(len(haystack)):
            if i + sub_len > len(haystack):
                break
            if haystack[i:i + sub_len] == needle:
                return i
        return -1
