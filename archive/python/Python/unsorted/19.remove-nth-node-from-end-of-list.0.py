# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n <= 0 or not head:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        i = 0
        while i < n:
            head = head.next
            i += 1
        predelete = dummy
        while head:
            head = head.next
            predelete = predelete.next
        predelete.next = predelete.next.next
        return dummy.next
