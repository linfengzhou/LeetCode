# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# from linkedlist import *


class Solution(object):

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        slow, fast = dummy, dummy
        count = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            count += 1
        # case 1: fast is None, odd len
        if not fast:
            length = count * 2 - 1
        # case 2: fast next is None, even len
        else:
            length = count * 2
        k = (k - 1) % length + 1
        break_point = length - k
        if break_point <= 0:
            return dummy.next
        slow = dummy
        while break_point > 0:
            slow = slow.next
            break_point -= 1
        new_head = slow.next
        slow.next = None
        dummy.next = new_head
        while new_head.next:
            new_head = new_head.next
        new_head.next = head
        return dummy.next

# if __name__ == '__main__':
#     a = generate_linkedlist([1, 2])
#     s = Solution()
#     q = s.rotateRight(a, 3)
#     while q:
#         print(q.val)
#         q = q.next
