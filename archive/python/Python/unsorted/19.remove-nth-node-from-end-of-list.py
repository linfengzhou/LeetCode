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
        if not head:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        count = 0
        while head:
            count += 1
            head = head.next
        node_before_remove = count - n
        head = dummy
        while node_before_remove > 0:
            head = head.next
            node_before_remove -= 1
        head.next = head.next.next
        return dummy.next
