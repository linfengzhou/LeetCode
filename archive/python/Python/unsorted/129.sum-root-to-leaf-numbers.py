# Definition for a binary tree node.


# class TreeNode(object):

#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        path, res = '', []
        self.dfs(root, path, res)
        res_list = list(map(lambda x: int(x), res))
        return sum(res_list)

    def dfs(self, root, path, res):
        if not root:
            return
        if not root.left and not root.right:
            return res.append(path + str(root.val))

        if root.left:
            self.dfs(root.left, path + str(root.val), res)
        if root.right:
            self.dfs(root.right, path + str(root.val), res)

# if __name__ == '__main__':
#     a = TreeNode(1)
#     a.left = TreeNode(2)
#     a.right = TreeNode(3)
#     b = Solution()
#     print(b.sumNumbers(a))
