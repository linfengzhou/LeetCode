# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        balance, max_diff = self.helper(root)
        return balance

    def helper(self, root):
        if not root:
            return True, 0

        # divide and conquer
        left_balance, left_max_depth = self.helper(root.left)
        right_balance, right_max_depth = self.helper(root.right)

        if (not left_balance) or (not right_balance):
            return False, -1
        if abs(left_max_depth - right_max_depth) > 1:
            return False, -1

        return True, max(left_max_depth, right_max_depth) + 1
