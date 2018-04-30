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
        first = 0
        for index in range(len(str)):
            if str[index] == " ":
                str[first: index] = reversed(str[first:index])
                first = index + 1
        str[first: index + 1] = reversed(str[first: index + 1])
        str.reverse()
