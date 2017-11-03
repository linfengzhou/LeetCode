class Solution(object):

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in range(n-1):
            s = self.helper(s)
        return s

    def helper(self, s):
        # '1'-->'11'-->'21'-->'1211'
        count = 0
        total = ''
        current = '#'
        for i in range(len(s)):
            if current == '#':
                count = 1
                current = s[i]
            elif current == s[i]:
                count += 1
            else:
                total += str(count)
                total += s[i - 1]
                count = 1
                current = s[i]
        total += str(count)
        total += s[i]
        return total
