class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs or len(strs) == 0:
            return ''
        for i in range(len(strs)):
            if i == 0:
                longest_len = len(strs[0])
            else:
                temp_str = strs[i]
                longest_len = min(longest_len, len(temp_str))
                j = 0
                while j < longest_len and temp_str[j] == strs[i - 1][j]:
                    j += 1
                longest_len = j
        return strs[0][0: longest_len]
