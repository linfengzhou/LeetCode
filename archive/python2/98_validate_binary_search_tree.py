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
        :rtype: bool
        """
        if not root:
            return []
        level, bfshelper = [], [root]

        while bfshelper != []:
            queue_size = len(bfshelper)
            i = 0
            level.append([])
            while i < queue_size:
                temp_node = bfshelper.pop(0)
                level[-1].append(temp_node.val)  # cost more efficience
                if temp_node.left:
                    bfshelper.append(temp_node.left)
                if temp_node.right:
                    bfshelper.append(temp_node.right)
                i += 1
        return level


class Solution(object):

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return []
        result, queue = [], [root]
        while len(queue) != 0:
            level = []
            i, size = 0, len(queue)
            while i < size:
                temp_node = queue.pop(0)
                level.append(temp_node.val)
                if temp_node.left:
                    queue.append(temp_node.left)
                if temp_node.right:
                    queue.append(temp_node.right)
                i += 1
            result.append(level)
        return result
