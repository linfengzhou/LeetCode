# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = []
        stack = []

        while root or len(stack) != 0:
            while root:
                stack.append(root)
                root = root.left

            temp_node = stack.pop()
            res.append(temp_node.val)
            root = temp_node.right

        for i in range(len(res)):
            if i != 0 and res[i - 1] >= res[i]:
                return False
        return True
