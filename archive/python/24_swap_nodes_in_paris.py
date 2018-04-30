# Definition for singly - linked list.


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while p.next and p.next.next:
            tmp = p.next.next
            p.next.next = tmp.next
            tmp.next = p.next
            p.next = tmp
            p = p.next.next
        return dummy.next


# class Solution:
#     # @param a ListNode
#     # @return a ListNode

#     def swapPairs(self, head):
#         if head == None or head.next == None:
#             return head
#         dummy = ListNode(0)
#         dummy.next = head
#         p = dummy
#         while p.next and p.next.next:
#             tmp = p.next.next
#             p.next.next = tmp.next
#             tmp.next = p.next
#             p.next = tmp
#             p = p.next.next
#         return dummy.next


# p pn pnn tmp tmpn
# 0 1  2    2   3
# 0 1  3    2   1
# 0 2  1    2   1
# 1 3  4    4   5
# 1 3  5    4   5
# 1 3  5    4   3
# 1 4  3    4   3
# 3 5  6    6
