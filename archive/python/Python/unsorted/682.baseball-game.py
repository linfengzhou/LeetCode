class Solution(object):

    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        new_ops = []
        for point in ops:
            if point == 'C':
                new_ops.pop()
            elif point == 'D':
                new_ops.append(new_ops[-1] * 2)
            elif point == '+':
                new_ops.append(new_ops[-1] + new_ops[-2])
            else:
                point = int(point)
                new_ops.append(point)
        return sum(new_ops)
# if __name__ == '__main__':
#     a = Solution()
#     print(a.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]
#                       ))
