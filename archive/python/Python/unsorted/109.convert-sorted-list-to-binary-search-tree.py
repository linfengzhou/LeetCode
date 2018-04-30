# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def __init__(self):
        self.current = None

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def getListLength(head):
            size = 0
            while head:
                head = head.next
                size += 1
            return size
        self.current = head
        size = getListLength(head)
        return self.dfs(size)

    def dfs(self, size):
        if size <= 0:
            return None

        left = self.dfs(size / 2)
        root = TreeNode(self.current.val)
        self.current = self.current.next
        right = self.dfs(size - 1 - size / 2)
        root.left = left
        root.right = right
        return root
