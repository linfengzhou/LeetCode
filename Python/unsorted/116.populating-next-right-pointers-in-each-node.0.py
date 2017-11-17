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
            return
        self.helper(root)

    def helper(self, root):
        if not root:
            return
        left = root
        while left:
            cur = left
            while cur:
                if not cur.left:
                    return
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left

                cur = cur.next
            left = left.left
