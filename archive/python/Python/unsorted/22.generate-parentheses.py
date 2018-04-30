class Solution(object):

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        current = ''
        self.helper(n, n, current, res)
        return res

    def helper(self, left, right, current, res):
        if left == 0 and right == 0:
            res.append(current)
        if right < left:
            return
        if left > 0:
            self.helper(left - 1, right, current + '(', res)
        if right > 0:
            self.helper(left, right - 1, current + ')', res)
