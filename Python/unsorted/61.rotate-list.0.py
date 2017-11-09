# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head
        count = 1
        slow = head
        while slow.next:
            slow = slow.next
            count += 1
        slow.next = head
        k = k % count
        count = count - k
        while count > 0:
            slow = slow.next
            count -= 1
        new_head = slow.next
        slow.next = None
        return new_head
