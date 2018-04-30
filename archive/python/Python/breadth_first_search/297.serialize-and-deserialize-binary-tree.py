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
        if not root:
            return []
        queue = [root]
        index = 0
        while index < len(queue):
            # node = queue.pop(0) #cannot use this method
            node = queue[index]
            if node:
                queue.append(node.left)
                queue.append(node.right)
            index += 1

        while not queue[-1]:
            queue.pop()

        return ','.join([str(node.val) if node else 'null' for node in queue])

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        vals = data.split(',')
        root = TreeNode(int(vals[0]))
        queue = [root]
        index = 0
        is_left = True
        for val in vals[1:]:
            if val != 'null':
                node = TreeNode(val)
                if is_left:
                    queue[index].left = node
                else:
                    queue[index].right = node
                queue.append(node)
            if not is_left:
                index += 1
            is_left = not is_left
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
