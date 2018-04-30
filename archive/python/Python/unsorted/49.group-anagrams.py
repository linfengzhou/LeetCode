class Solution(object):

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs or len(strs) == 0:
            return 0

        strs_dict = {}
        for char in strs:
            new_char = ''.join(sorted(char))
            if new_char not in strs_dict:
                strs_dict[new_char] = [char]
            else:
                strs_dict[new_char].append(char)
        return strs_dict.values()
