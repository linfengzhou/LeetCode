# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        path = []
        res = []
        if not root:
            return res
        self.helper(root, sum, path, res)
        return res

    def helper(self, root, target, path, res):
        if not root:
            return False
        if root.left is None and root.right is None:
            if root.val == target:
                res.append(path + [root.val])
            return

        path.append(root.val)
        self.helper(root.left, target - root.val, path, res)
        self.helper(root.right, target - root.val, path, res)
        path.pop()

        return
