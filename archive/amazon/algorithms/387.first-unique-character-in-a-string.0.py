class Solution(object):

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_dict = dict()
        for index, char in enumerate(s):
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
        for index, char in enumerate(s):
            if char_dict[char] == 1:
                return index
        return -1
