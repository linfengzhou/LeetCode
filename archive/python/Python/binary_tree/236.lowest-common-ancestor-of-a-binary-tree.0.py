# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# what if p or q not in the tree


class Solution(object):

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        lca, is_p, is_q = self.helper(root, p, q)
        if is_p and is_q:
            return lca
        else:
            return None

    def helper(self, root, p, q):
        if not root:
            return root, False, False

        left_lca, left_p, left_q = self.helper(root.left, p, q)
        right_lca, right_p, right_q = self.helper(root.right, p, q)

        is_p = left_p or right_p or root == p
        is_q = left_q or right_q or root == q

        if left_lca and right_lca:
            return root, is_p, is_q
        if left_lca:
            return left_lca, is_p, is_q
        if right_lca:
            return right_lca, is_p, is_q

        return None, is_p, is_q
