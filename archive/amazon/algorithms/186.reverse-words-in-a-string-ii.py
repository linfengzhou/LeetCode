class Solution(object):

    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        # first loop: reverse each string
        # second: reverse the whole string
        if not str or len(str) == 0:
            return

        def reverse_string(l, r):
            while l < r:
                str[l], str[r] = str[r], str[l]
                l += 1
                r -= 1
        first = 0
        for index in range(len(str)):
            if str[index] == " ":
                reverse_string(first, index - 1)
                first = index + 1
        reverse_string(first, index)
        reverse_string(0, len(str) - 1)
