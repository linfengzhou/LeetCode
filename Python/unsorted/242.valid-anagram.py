class Solution(object):

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = dict()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1
        for j in range(len(t)):
            if t[j] not in s_dict:
                return False
            elif s_dict[t[j]] == 1:
                s_dict.pop(t[j])
            else:
                s_dict[t[j]] -= 1
        return len(s_dict) == 0

# if __name__ == '__main__':
#     a = Solution()
#     print(a.isAnagram('abva', 'vba'))
