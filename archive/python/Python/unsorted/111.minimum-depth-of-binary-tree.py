import sys
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.dfs(root)

    def dfs(self, root):
        if not root:
            return sys.maxsize

        if not root.left and not root.right:
            return 1

        return min(self.dfs(root.left), self.dfs(root.right)) + 1
