# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        # preorder: root -> left -> right
        # inorder: left -> root -> right
        if len(preorder) != len(inorder):
            return None
        result = self.dfs(preorder, inorder, 0, len(
            preorder) - 1, 0, len(inorder) - 1)
        return result

    def dfs(self, preorder, inorder, prestart, preend, instart, inend):
        if instart > inend:
            return None
        root = TreeNode(preorder[prestart])
        position = self.find_position(inorder, instart, inend, root.val)
        root.left = self.dfs(
            preorder, inorder,
            prestart + 1, prestart + position - instart,
            instart, position - 1
        )
        root.right = self.dfs(
            preorder, inorder,
            prestart + position - instart + 1, preend,
            position + 1, inend)
        return root

    def find_position(self, inorder, instart, inend, p_val):
        i = instart
        while i <= inend:
            if inorder[i] == p_val:
                return i
            i += 1
        return -1
