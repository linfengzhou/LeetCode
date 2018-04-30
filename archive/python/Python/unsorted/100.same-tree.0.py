# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        stack = [p, q]
        while len(stack) != 0:
            q_cur = stack.pop()
            p_cur = stack.pop()
            if not p and not q:
                continue
            if not p or not q:
                return False
            if p_cur.val != q_cur.val:
                return False
            stack.append(p.left)
            stack.append(q.left)
            stack.append(p.right)
            stack.append(q.right)
        return True
