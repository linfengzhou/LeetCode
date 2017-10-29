# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        result = self.helper(root, sum)
        return result

    def helper(self, root, target):
        if not root:
            return False
        if root.left is None and root.right is None:
            if target  == root.val:
                return True
            else:
                return False

        left = self.helper(root.left, target - root.val)
        right = self.helper(root.right, target - root.val)

        return left or right
