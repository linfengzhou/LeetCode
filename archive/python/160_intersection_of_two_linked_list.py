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
        if not headA or not headB:
            return None
        p1 = headA
        p2 = headB
        count_a, count_b = 0, 0
        while p1 is not None:
            count_a = count_a + 1
            p1 = p1.next
        while p2 is not None:
            count_b = count_b + 1
            p2 = p2.next
        if count_a > count_b:
            n = count_a - count_b
            while n > 0:
                headA = headA.next
                n = n - 1
        else:
            n = count_b - count_a
            while n > 0:
                headB = headB.next
                n = n - 1
        while (headA is not None) or (headB is not None):
            if headA.next == headB.next and headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return None


# solution 2
# because if there is an intersection,
# at least the last node of both linked list should be the same
# therefore create two pointers to iterate two linked list, at the first time,
# once iterate all nodes of one linked list
# the pointer will equal to the head of another linked list,
# and if another iteration is over,
# the pointer will equal to the another one.
# This method make sure in the second iteration process, we must find the
# intersaction.
# This logic is the same to our first logic. make sure the second
# iteration have the same length
