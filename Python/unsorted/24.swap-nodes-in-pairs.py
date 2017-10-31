# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        current = dummy
        while current and current.next and current.next.next:
            temp = current.next
            current.next = current.next.next
            temp.next = current.next.next
            current.next.next = temp
            current = current.next.next
        return dummy.next
