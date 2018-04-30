import json
# Definition for singly-linked list.


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


class Solution(object):

    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
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
        for i in range(k):
            temp = []
            if parts < larger:
                for j in range(smaller + 1):
                    temp.append(root.val)
                    root = root.next
                parts += 1
                res.append(temp)
            else:
                for j in range(max(smaller, 1)):
                    if not root:
                        continue
                    else:
                        temp.append(root.val)
                        root = root.next
                res.append(temp)
        return res

# if __name__ == '__main__':
#     a = Solution()
#     print(a.splitListToParts(stringToListNode("[]"), 5))
