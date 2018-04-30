class Solution(object):

    def titleToNumber(self, s):
        if not s:
            return 0
        w2c = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        col = 0
        count = 0
        s = list(s)
        s.reverse()
        for i, c in enumerate(s):
            col = col + (w2c.index(c) + 1) * 26 ** i
        return col
