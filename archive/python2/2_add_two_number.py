# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        root = ListNode(0)
        head = root
        while l1 is not None or l2 is not None or carry != 0:
            v1 = v2 = 0
            if l1 is not None:
                v1 = l1.val
                l1 = l1.next
            if l2 is not None:
                v2 = l2.val
                l2 = l2.next
            cur = v1 + v2 + carry
            carry = cur / 10
            cur = cur % 10
            root.next = ListNode(cur)
            root = root.next
        return head.next
