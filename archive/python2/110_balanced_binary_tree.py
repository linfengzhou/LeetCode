# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# my version: based on maximumn depth


class Solution(object):

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if self.isBalanced(root.left) and \
                self.isBalanced(root.right) and \
                abs(self.dfs(root.left) - self.dfs(root.right)) <= 1:
            return True

        return False

    def dfs(self, root):
        if root is None:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        return max(left, right) + 1

# nine chapter version


class Solution(object):

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        balanced, height = self.validate(root)
        return balanced

    def validate(self, root):
        if root is None:
            return True, 0

        left_balance, left_height = self.validate(root.left)
        if not left_balance:
            return False, 0
        right_balance, right_height = self.validate(root.right)
        if not right_balance:
            return False, 0

        return abs(left_height - right_height) <= 1, max(left_height, right_height) + 1


class Solution(object):

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        balanced, height = self.validate(root)
        return balanced

    def validate(self, root):
        if root is None:
            return True, 0

        left_balance, left_height = self.validate(root.left)
        if not left_balance:
            return False, 0
        right_balance, right_height = self.validate(root.right)
        if not right_balance:
            return False, 0

        return abs(left_height - right_height) <= 1, max(left_height, right_height) + 1
