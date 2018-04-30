
class Solution(object):

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or m > n:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        head, count = dummy, 0
        count = 0

        while head.next and count < m - 1:
            count += 1
            head = head.next

        preNode, postNode = head, head.next

        while preNode and postNode and postNode.next and count < n - 1:

            count += 1
            new = postNode.next
            postNode.next = new.next
            new.next = preNode.next
            preNode.next = new

        return dummy.next
