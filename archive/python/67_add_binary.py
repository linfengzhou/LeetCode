# one line solution
class Solution(object):

    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]

# recursion


class Solution(object):

    def addBinary(self, a, b):

        # https://discuss.leetcode.com/topic/6207/an-accepted-concise-python-recursive-solution-10-lines
