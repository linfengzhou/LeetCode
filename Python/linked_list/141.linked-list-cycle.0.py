# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
        	return False
        node_set = set()
        while head:
        	if head in node_set:
        		return True
        	else:
        		node_set.add(head)
        	head = head.next
        return False