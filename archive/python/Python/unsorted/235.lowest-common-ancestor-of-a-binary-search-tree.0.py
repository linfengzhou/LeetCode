# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        small = p.val if p.val < q.val else q.val
        large = p.val if p.val > q.val else q.val
        while not(root.val >= small and root.val <= large):
            if root.val > small:
                root = root.left
            else:
                root = root.right
        return root
