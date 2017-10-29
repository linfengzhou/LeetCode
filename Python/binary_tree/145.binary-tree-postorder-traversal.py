# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result = self.helper(root)
        return result

    def helper(self, root):
        result = []
        if not root:
            return

        # divide
        left = self.helper(root.left)
        right = self.helper(root.right)

        if left:
            result += left
        if right:
            result += right
        result.append(root.val)
        return result
