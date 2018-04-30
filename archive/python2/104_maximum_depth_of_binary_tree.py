# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Version I: Traverse


class Solution(object):

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_depth = 0
        self.dfs(root, 1)  # cur_depth 1
        return self.max_depth

    def dfs(self, node, cur_depth):
        if node is None:
            return 0

        self.max_depth = max(self.max_depth, cur_depth)
        self.dfs(node.left, cur_depth + 1)
        self.dfs(node.right, cur_depth + 1)


# Version II: Divide and Conquer
class Solution(object):

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        # divide
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        # conquer
        return max(left, right) + 1
