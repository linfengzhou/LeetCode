class Solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ROMAN = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        if not s or s == '':
            return 0
        n = len(s)
        res = ROMAN[s[n - 1]]
        for i in range(n - 2, -1, -1):
            if ROMAN[s[i]] < ROMAN[s[i + 1]]:
                res -= ROMAN[s[i]]
            else:
                res += ROMAN[s[i]]
        return res
