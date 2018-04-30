# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    # step 1 递归的定义

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        # step 3 递归的出口
        if not root:
            return res

        if (not root.left) and (not root.right):
            res.append(str(root.val))

        # Step 2: 递归的拆解
        # Divide
        leftPaths = self.binaryTreePaths(root.left)  # "2->5"
        rightPaths = self.binaryTreePaths(root.right)  # "3"

        # Conquer
        for path in leftPaths:
            res.append(str(root.val) + '->' + path)
        for path in rightPaths:
            res.append(str(root.val) + '->' + path)

        return res
