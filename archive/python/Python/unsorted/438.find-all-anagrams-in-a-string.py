class Solution(object):

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        p_dict = dict()
        for char in p:
            if char not in p_dict:
                p_dict[char] = 1
            else:
                p_dict[char] += 1
        i, len_p = 0, len(p)
        temp_dict = dict()
        res = []
        while i < len(s):
            temp_dict.setdefault(s[i], 0)
            temp_dict[s[i]] += 1
            if i > len_p - 1:
                temp_dict[s[i - len_p]] -= 1
                if temp_dict[s[i - len_p]] == 0:
                    temp_dict.pop(s[i - len_p])
            if i >= len_p - 1:
                if temp_dict == p_dict:
                    res.append(i - len_p + 1)
            i += 1
        return res
if __name__ == '__main__':
    a = Solution()
    print([a:a])
