class Solution(object):

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        stack, res = [], []
        x, l = 1, 0
        while True:
            if l == k:
                res.append(stack[:])
            if l == k or n - x + 1 < k - l:
                if len(stack) == 0:
                    return res
                x = stack.pop() + 1
                l -= 1
            else:
            	stack.append(x)
                x += 1
                l += 1
