# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


def generate_linkedlist(nums):
    if not nums:
        return ListNode(None)
    dummy = ListNode(-1)
    head = dummy
    for num in nums:
        head.next = ListNode(num)
        head = head.next
    return dummy.next

# if __name__ == '__main__':
#     a = [1, 2, 3, 4, 5]
#     test = generate_linkedlist(a)
#     while test:
#         print(test.val)
#         test = test.next
