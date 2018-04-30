class Solution(object):

        # my solution

    # def longestCommonPrefix(self, strs):
    #     if not strs:
    #         return ""
    #     check = strs[0]
    #     for i, c in enumerate(check):
    #         for item in strs[1:]:
    #             if not (check[:i + 1] in item[:i + 1]):
    #                 return check[:i]
    #     return check

    # better solution: instead of using slicing, check each character
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        check = min(strs, key=len)
        for i, c in enumerate(check):
            for item in strs:
                if check[i] != item[i]:
                    return check[:i]
        return check
