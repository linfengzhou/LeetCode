# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        result = self.dfs(p, q)
        return result

    def dfs(self, p, q):
        if (not p) ^ (not q):
            return False
        if not p and not q:
            return True
        if p.val != q.val:
            return False
        if (not p.left and q.left) or (p.left and not q.left):
            return False
        if (not p.right and q.right) or (p.right and not q.right):
            return False

        left = self.dfs(p.left, q.left)
        right = self.dfs(p.right, q.right)

        if not left or not right:
            return False
        return True
