class Solution(object):

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        number_map = {'2': ['a', 'b', 'c'],
                      '3': ['d', 'e', 'f'],
                      '4': ['g', 'h', 'i'],
                      '5': ['j', 'k', 'l'],
                      '6': ['m', 'n', 'o'],
                      '7': ['p', 'q', 'r', 's'],
                      '8': ['t', 'u', 'v'],
                      '9': ['w', 'x', 'y', 'z']
                      }
        res = []
        if digits == '':
            return res
        self.dfs('', digits, res, number_map, 0)
        return res

    def dfs(self, string_cb, digits, res, number_map, num):
        if num == len(digits):
            res.append(string_cb)
            return

        for letter in number_map[digits[num]]:
            self.dfs(string_cb + letter, digits, res, number_map, num + 1)
