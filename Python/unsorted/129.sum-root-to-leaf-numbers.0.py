# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return self.dfs(root, 0)

    def dfs(self, root, total):
        if not root:
            return 0

        if not root.left and not root.right:
            return total * 10 + root.val

        return self.dfs(
            root.left, total * 10 + root.val
        ) + self.dfs(
            root.right, total * 10 + root.val
        )
