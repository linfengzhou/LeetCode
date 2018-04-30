# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# head_1 = l1
# head_2 = l2
# switch = False
# while (head_1.next is not None) and (head_2.next is not None):
#     if switch == False:
#         if head_1.val != head_1.next.val:
#             if head_1.val == head_2.val:
#             	res = head_1.next
#                 head_1.next = head_2
#                 switch = True
#             elif head_1.next.val > head_2.val:
#             	res = head_1.next
#             	head_1.next = head_2
#             	switch = True
#         head_1 = head_1.next
#     else:
#     	if head_2.val != head_2.next.val:
#     		if


class Solution(object):

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        total = merge = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                merge.next = l1
                l1 = l1.next
            else:
                merge.next = l2
                l2 = l2.next
            merge = merge.next
        # last one
        merge.next = l1 or l2
        return merge.next


class Solution(object):

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = mergeTwoLists(l2.next, l1)
            return l2
