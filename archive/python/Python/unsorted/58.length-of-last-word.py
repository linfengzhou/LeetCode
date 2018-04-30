class Solution(object):

    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 0:
            return 0
        n_s = len(s)
        i = len(s) - 1
        total_len = 0
        count_sp = 0
        while i >= 0:
            if s[i].isalpha():
                total_len += 1
            elif s[i] == ' ':
                if total_len == 0:
                    pass
                else:
                    return total_len
            i -= 1
        return total_len

# if __name__ == '__main__':
#     a = Solution()
#     print(a.lengthOfLastWord('"a "'))
