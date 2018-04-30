# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing

    def connect(self, root):
        if not root:
            return None

        while root:
            next_node = None  # the first node of next level
            prev_node = None  # previous node on the same level
            while root:
                if not next_node:
                    if root.left:
                        next_node = root.left
                    else:
                        next_node = root.right
                if root.left:
                    if prev_node:
                        prev_node.next = root.left
                    #     prev_node = prev_node.next
                    # else:
                    prev_node = root.left
                if root.right:
                    if prev_node:
                        prev_node.next = root.right
                    #     prev_node = prev_node.next
                    # else:
                    prev_node = root.right
                root = root.next
            root = next_node
