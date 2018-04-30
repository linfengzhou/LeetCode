class Solution(object):

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if (root is None or root == p or root == q):
            return root

        # divide
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # concuqer
        if left is not None and right is not None:
            return root
        if left is not None:
            return left
        if right is not None:
            return right

        return None
