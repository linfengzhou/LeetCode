# my solution (tle)
class Solution(object):

    def reverseString(self, s):
        new_s = ''
        if s:
            s_len = len(s)
            for index in range(s_len):
                new_s = s[index] + new_s
        return new_s


class Solution(object):

    def reverseString(self, s):
        return s[::-1]

# a better solution


class Solution(object):

    def reverseString(self, s):
        s = list(s)
        n = len(s) - 1
        i = 0
        while n > i:
            s[i], s[n] = s[n], s[i]
            i = i + 1
            n = n - 1
        return ''.join(s)
