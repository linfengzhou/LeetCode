# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # find tail of A
        if not headA or not headB:
            return None
        head = headA
        while head.next:
            head = head.next
        tail = head
        tail.next = headB
        # find entrance of the circle
        result = self.findEntrance(headA)
        # retain original structure
        tail.next = None
        return result

    def findEntrance(self, head):
        slow, fast, slow2 = head, head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if not fast or not fast.next:
            return None
        while slow != slow2:
            slow = slow.next
            slow2 = slow2.next
        return slow
