# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        stack = [root]
        # stack is not empty
        while len(stack) != 0:
            temp_node = stack.pop()
            res.append(temp_node.val)
            if temp_node.right:
                stack.append(temp_node.right)
            if temp_node.left:
                stack.append(temp_node.left)
        return res
