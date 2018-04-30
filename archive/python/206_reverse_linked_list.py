# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = None
        while head:
            head.next, res, head, = res, head, head.next
        return res


class Solution(object):

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = None
        while head is not None:
            next_ele = head.next
            if res is None:
                head.next = None
                res = head
            else:
                head.next = res
                res = head
            head = next_ele
        return res

# store head.next first
# made the head.next = res
# made the res = head
# make the head = head.next(from the stored data)


# how to to do it by recursion???
