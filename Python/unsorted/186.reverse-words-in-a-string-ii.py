class Solution(object):

    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        if not str:
            return
        n = len(str)
        count = 0
        first = 0
        while count < n:
            if str[count] == ' ':
                last = count - 1
                while first < last:
                    str[first], str[last] = str[last], str[first]
                    first += 1
                    last -= 1
                first = count + 1
            count += 1
        last = count - 1
        while first < last:
            str[first], str[last] = str[last], str[first]
            first += 1
            last -= 1
        i, j = 0, n - 1
        while i < j:
            str[i], str[j] = str[j], str[i]
            i += 1
            j -= 1
