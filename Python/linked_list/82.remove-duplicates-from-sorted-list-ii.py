# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        head = dummy
        while head.next and head.next.next:
            if (head.next.val == head.next.next.val):
                temp_val = head.next.val
                while(head.next and head.next.val == temp_val):
                    head.next = head.next.next
            else:
                head = head.next
        return dummy.next
