# Definition for singly-linked list.


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        if not root:
            return [[]] * k
        slow, fast = root, root
        count, res = 0, []
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            count += 1
        # 1, 2, 3, 4, 5      fast.next => NONE
        # 1, 2, 3, 4, 5, 6   fast => NONE
        if fast:
            count = count * 2 + 1
        else:
            count = count * 2

        larger = count % k
        smaller = count // k
        parts = 0
        curr = root

        for i in range(k):
            if parts < larger:
                loops = smaller + 1
            else:
                loops = smaller

            res.append(curr)

            for j in range(loops):
                if not curr:
                    continue
                else:
                    prev = curr
                    curr = curr.next
            prev.next = None
            parts += 1
        return res

# if __name__ == '__main__':
#     a = Solution()
#     print(
#         listNodeArrayToString(
#             a.splitListToParts(stringToListNode("[1,2,3,4]"), 5)))
