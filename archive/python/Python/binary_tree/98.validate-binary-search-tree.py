# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys


class Solution(object):

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        balance, min_value, max_value = self.helper(root)
        return balance

    def helper(self, root):
        if not root:
            return True, sys.maxint, -sys.maxint

        left_balance, left_min, left_max = self.helper(root.left)
        right_balance, right_min, right_max = self.helper(root.right)

        if (left_balance and right_balance)\
                and (root.val > left_max)\
                and (root.val < right_min):
            return True, min(root.val, left_min), max(right_max, root.val)
        return False, -1, -1
