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
        count, i = 1, 1
        node = head
        while node.next is not None:
            node = node.next
            count = count + 1
        if count == n:
            return head.next
        root = head
        while True:
            if i == count - n:
                if n == 1:
                    head.next = None
                else:
                    head.next = head.next.next
                break
            i = i + 1
            head = head.next
        return root


# better solution 1
# two pointer
class Solution(object):

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        fast, slow = dummy, dummy
        for i in range(n):
            fast = fast.next

        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next
