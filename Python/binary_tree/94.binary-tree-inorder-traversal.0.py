# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        self.dfs(root, res)
        return res

    def dfs(self, root, res):
        if root.left:
            self.dfs(root.left, res)
        res.append(root.val)
        if root.right:
            self.dfs(root.right, res)
