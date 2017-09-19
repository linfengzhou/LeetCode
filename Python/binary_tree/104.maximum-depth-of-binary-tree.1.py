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
        res = [0]
        if not root:
            return res[0]

        self.helper(root, 1, res)
        return res[0]

    def helper(self, root, cur_depth, res):
        if not root:
            return

        if cur_depth > res[0]:
            res[0] = cur_depth

        self.helper(root.left, cur_depth + 1, res)
        self.helper(root.right, cur_depth + 1, res)
        