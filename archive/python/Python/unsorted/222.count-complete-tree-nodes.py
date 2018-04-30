# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.leftDepth(root)
        right = self.rightDepth(root)
        if left == right:
            return (1 << left) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def leftDepth(self, root):
        dep = 0
        while root:
            root = root.left
            dep += 1
        return dep

    def rightDepth(self, root):
        dep = 0
        while root:
            root = root.right
            dep += 1
        return dep
