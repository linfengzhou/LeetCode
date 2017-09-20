# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        res = []
        stack = [root]
        while len(stack) != 0:
            temp_node = stack.pop()
            res.append(temp_node.val)
            if temp_node.right:
                stack.append(temp_node.right)
            if temp_node.left:
                stack.append(temp_node.left)
        for item in res[1:]:
            temp_node = TreeNode(item)
            root.left = None
            root.right = temp_node
            root = root.right
