# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        root = head
        if not head:
        	return head
        res = {}
        while head:
        	res.setdefault(head.label, RandomListNode(head.label))
        	head = head.next
        head = root
        dummy = RandomListNode(1)
        root = dummy
        while head:
        	new_node = res.get(head.label)
        	if head.next:
        		new_node.next = res.get(head.next.label)
        	if head.random:
        		new_node.random = res.get(head.random.label)
        	dummy.next = new_node
        	dummy = dummy.next
        	new_node = new_node.next
        	head = head.next
        return root.next



