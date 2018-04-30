# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # inorder: left -> root -> right
        # postorder: left -> right -> root
        if len(inorder) != len(postorder):
            return None
        return self.dfs(
            inorder, postorder,
            0, len(inorder) - 1,
            0, len(postorder) - 1)

    def find_position(self, inorder, instart, inend, p_val):
        index = 0
        while index <= inend:
            if inorder[index] == p_val:
                return index
            index += 1
        return -1

    def dfs(self, inorder, postorder, instart, inend, poststart, postend):
        # exit condition
        if instart > inend:
            return None

        root = TreeNode(postorder[postend])
        position = self.find_position(inorder, instart, inend, root.val)
        root.left = self.dfs(
            inorder, postorder,
            instart, position - 1,
            poststart, poststart + position - 1 - instart)
        root.right = self.dfs(
            inorder, postorder,
            position + 1, inend,
            poststart + position - instart, postend - 1,
        )
        return root
