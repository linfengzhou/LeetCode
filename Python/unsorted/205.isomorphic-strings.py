class Solution(object):

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_map = dict()
        t_map = dict()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in s_map:
                s_map[s[i]] = [i]
            else:
                s_map[s[i]].append(i)
            if t[i] not in t_map:
                t_map[t[i]] = [i]
            else:
                t_map[t[i]].append(i)
        return sorted(s_map.values()) == sorted(t_map.values())

# if __name__ == '__main__':
#     a = Solution()
#     print(a.isIsomorphic('aba', 'cdc'))
