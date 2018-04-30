class Solution(object):

    def romanToInt(self, s):
        # I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1,000.
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum_s = 0
        for i, c in enumerate(s):
            if (i < len(s) - 1) and (dic[c] < dic[s[i + 1]]):
                sum_s = sum_s - dic[c]
            else:
                sum_s = sum_s + dic[c]
        return sum_s

## the difference between &, and 
## 


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        res = 0
        for i, c in enumerate(s):
            if i < len(s) - 1 and roman[c] < roman[s[i + 1]]:
                res -= roman[c]
            else:
                res += roman[c]
        return res