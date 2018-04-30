import heapq
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        res = []
        for nodes in lists:
            if nodes:
                heapq.heappush(res, (nodes.val, nodes))
        dummy = ListNode(-1)
        head = dummy

        while len(res) != 0:
            new_node = heapq.heappop(res)[1]
            head.next = new_node
            head = head.next
            if new_node.next:
                heapq.heappush(res, (new_node.next.val, new_node.next))
        return dummy.next
