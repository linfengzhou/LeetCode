# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def reverse(self, head):
        dummy = ListNode(-1)
        dummy.next = head
        tail = dummy.next
        cur = tail.next
        while cur:
            prev_head = dummy.next
            new_head = cur
            dummy.next = new_head
            tail.next = new_head.next
            new_head.next = prev_head
            cur = tail.next
        return dummy.next

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        # find mid position
        slow, fast = head, head.next
        # 1-2-3-4 fast at 4 slow at 2
        # 1-2-3-4-5 fast at None slow at 3
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # cut to two part
        second = slow.next
        slow.next = None
        # reverse second part
        second = self.reverse(second)
        # merge two parts together
        # 1-2 4-3
        first = head
        while first.next:
            temp = first.next  # 2
            first.next = second  # 1-4
            temp2 = second.next
            second.next = temp  # 4-2
            first = temp  # 1-4-2
            second = temp2
        if second:
            first.next = second
