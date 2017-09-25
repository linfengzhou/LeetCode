# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        queue = [root]
        index = 0
        while len(queue) != 0:
            # node = queue.pop(0) #cannot use this method
            node = queue[index]
            if node:
                queue.append(node.left)
                queue.append(node.right)

        n = len(queue)

        while not queue[n - 1]:
            queue.pop()

        return str([str(node.val) if node else 'null' for node in queue])

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.strip('\n')
        vals = data[1:-1].split(',')
        if len(vals) == 0:
            return None
        root = TreeNode(int(vals[0]))


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
