# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        if not root:
            return self.res

        self.helper(root, 1)
        return self.res

    def helper(self, root, cur_depth):
        if not root:
            return

        if cur_depth > self.res:
            self.res = cur_depth

        self.helper(root.left, cur_depth + 1)
        self.helper(root.right, cur_depth + 1)
