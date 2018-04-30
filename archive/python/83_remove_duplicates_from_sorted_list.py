# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head
        res = head
        while res.next is not None:
            if res.val == res.next.val:
                res.next = res.next.next
            else:
                res = res.next
        return head   # return the first element of Linnked List

# a = ListNode(3)
# b = ListNode(3)
# c = ListNode(4)
# d = ListNode(4)
# e = ListNode(5)
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# print a.next.next.next.next.val

# if __name__ == "__main__":
#     print Solution.deleteDuplicates(a)
