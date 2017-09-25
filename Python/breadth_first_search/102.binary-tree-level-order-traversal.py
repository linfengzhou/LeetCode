# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res

        queue = [root]
        while len(queue) != 0:
            path = []
            i = 0
            queue_size = len(queue)
            while i < queue_size:
                temp_node = queue.pop(0)
                if temp_node.left:
                    queue.append(temp_node.left)
                if temp_node.right:
                    queue.append(temp_node.right)
                path.append(temp_node.val)
                i += 1
            res.append(path)
        return res
