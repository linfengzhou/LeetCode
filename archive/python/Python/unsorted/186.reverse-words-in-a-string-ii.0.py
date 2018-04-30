class Solution(object):

    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        if not str:
            return
        self.reverse(str, 0, len(str) - 1)
        count = 0
        start = 0
        while count < len(str):
            if str[count] == ' ':
                self.reverse(str, start, count - 1)
                start = count + 1
            count += 1

        self.reverse(str, start, len(str) - 1)

    def reverse(self, str, i, j):
        while i < j:
            str[i], str[j] = str[j], str[i]
            i += 1
            j -= 1
