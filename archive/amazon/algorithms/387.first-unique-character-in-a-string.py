class Solution(object):

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_dict = dict()
        for index, char in enumerate(s):
            if char not in char_dict:
                char_dict[char] = index
            else:
                char_dict[char] = -1
        min_index = len(s)
        for (i, v) in char_dict.items():
            if v == -1:
                continue
            else:
                min_index = min(min_index, v)
        if min_index == len(s):
            return -1
        else:
            return min_index
