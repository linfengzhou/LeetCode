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
            while nodes:
                heapq.heappush(res, nodes.val)
                nodes = nodes.next
        dummy = ListNode(-1)
        head = dummy
        while len(res) != 0:
            new_node = ListNode(heapq.heappop(res))
            head.next = new_node
            head = head.next
        return dummy.next
