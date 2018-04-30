class Solution(object):

    def generate(self, numRows):
        pascal_list = []
        if not numRows:
            return pascal_list
        if numRows == 0:
            return pascal_list
        pascal_list.append([1])
        if numRows == 1:
            return pascal_list
        pascal_list.append([1, 1])
        if numRows == 2:
            return pascal_list
        for row in range(2, numRows):
            current = []
            for i in range(row + 1):
                if i == 0:
                    current.append(1)
                elif i == row:
                    current.append(1)
                else:
                    current.append(pascal_list[row - 1][i - 1] +
                                   pascal_list[row - 1][i])
            pascal_list.append(current)
        return pascal_list
