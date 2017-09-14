# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head
        left_dummy, right_dummy = ListNode(0), ListNode(0)
        left, right = left_dummy, right_dummy

        while head:
            if head.val < x:
                left.next = ListNode(head.val)
                left = left.next
            else:
                right.next = ListNode(head.val)
                right = right.next
            head = head.next

        left.next = right_dummy.next
        return left_dummy.next
